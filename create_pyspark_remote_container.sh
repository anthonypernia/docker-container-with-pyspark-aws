docker run -it -v ~/.aws:/home/glue_user/.aws -v /Users/anthonypernia/Documents/projects/aws-local-pyspark-execution-docker-remote:/home/glue_user/workspace/ -e AWS_PROFILE=$PROFILE_NAME -e DISABLE_SSL=true --rm -p 4040:4040 -p 18080:18080 -p 5678:5678 --name glue_pyspark amazon/aws-glue-libs:glue_libs_4.0.0_image_01 pyspark

# docker run -it -v ~/.aws:/home/glue_user/.aws -v $PWD:/home/glue_user/workspace/jupyter_workspace/ -e AWS_PROFILE=$PROFILE_NAME -e DISABLE_SSL=true --rm -p 4040:4040 -p 18080:18080 -p 8998:8998 -p 8888:8888 -p 5678:5678 --name glue_jupyter_lab amazon/aws-glue-libs:glue_libs_4.0.0_image_01 /home/glue_user/jupyter/jupyter_start.sh


