"Authentication use case implementation."
import calendar
from datetime import datetime, timedelta
import json
from typing import Any

from argon2 import PasswordHasher

from jwcrypto import jwk, jwt

from opentelemetry import trace

from promotion import settings


SERVER = trace.SpanKind.SERVER


class AuthenticationUseCase:
    """Implements small subset of OAuth2 password grant with JWT."""

    def __init__(self, user_use_case, tracer) -> None:
        self.user = user_use_case
        self.tracer = tracer

    def authenticate(self, email: str, password: str) -> Any:
        """Authenticate password for the given user email"""
        with self.tracer.start_as_current_span(
            "AuthenticateUseCase.authenticate", kind=SERVER
        ) as span:
            ph = PasswordHasher()
            user = self.user.retrieve_user_by_email(email)
            ph.verify(user.password, password)
            span.set_attribute("authenticated?", str(True))
            key = jwk.JWK.from_pem(
                str(
                    settings.RSA_PRIVATE_KEY.encode("utf8").decode("unicode-escape")
                ).encode("utf8")
            )
            expiration_time = datetime.utcnow() + timedelta(
                seconds=settings.ID_TOKEN_EXPIRE_SECONDS
            )
            # Required ID Token claims
            claims = {
                "iss": settings.ISS_ENDPOINT,
                "sub": str(user.email),
                "aud": user.email,
                "exp": int(calendar.timegm(expiration_time.utctimetuple())),
                "iat": int(calendar.timegm(datetime.utcnow().utctimetuple())),
                "auth_time": int(calendar.timegm(expiration_time.utctimetuple())),
            }

            jwt_token = jwt.JWT(
                header=json.dumps({"alg": "RS256"}, default=str),
                claims=json.dumps(claims, default=str),
            )
            jwt_token.make_signed_token(key)
            return jwt_token.serialize()
