ENV = /usr/bin/env

.SHELLFLAGS = -c # Run commands in a -c flag
.SILENT: ; # no need for @
.ONESHELL: ; # recipes execute in same shell
.NOTPARALLEL: ; # wait for this target to finish
.EXPORT_ALL_VARIABLES: ; # send all vars to shell

.PHONY: all # All targets are accessible for user
.DEFAULT: help # Running Make will run the help target

help: ## Show Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

generate-v1alpha1:
	mkdir -p ../promotion/grpc/v1alpha1
	python -m grpc_tools.protoc -I. -I.third_party/googleapis -Ipromotion/grpc/v1alpha1/ --python_out=. --grpc_python_out=. promotion/grpc/v1alpha1/discount.proto
	python -m grpc_tools.protoc -I. -I.third_party/googleapis -Ipromotion/grpc/v1alpha1/ --python_out=. --grpc_python_out=. promotion/grpc/v1alpha1/promotion_api.proto
	rm promotion/grpc/v1alpha1/discount_pb2_grpc.py
	mv promotion/grpc/v1alpha1/*.py ../promotion/grpc/v1alpha1

generate-v1alpha2:
	mkdir -p ../promotion/grpc/v1alpha2
	python -m grpc_tools.protoc -I. -I.third_party/googleapis -Ipromotion/grpc/v1alpha2/ --python_out=. --grpc_python_out=. promotion/grpc/v1alpha2/discount.proto
	python -m grpc_tools.protoc -I. -I.third_party/googleapis -Ipromotion/grpc/v1alpha2/ --python_out=. --grpc_python_out=. promotion/grpc/v1alpha2/promotion_api.proto
	rm promotion/grpc/v1alpha2/discount_pb2_grpc.py
	mv promotion/grpc/v1alpha2/*.py ../promotion/grpc/v1alpha2

generate: generate-v1alpha1 generate-v1alpha2 ## Genereate gRPC stubs
 
generate-go: ## Genereate gRPC stubs gor golang
	prototool generate
	mv ../../product/grpc/client/promotion/grpc/v1alpha1 ../../product/grpc/client/promotion
	rm -r ../../product/grpc/client/promotion/grpc
