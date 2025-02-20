#!/bin/sh

poetry version $1
version=$(poetry version --short)

git diff HEAD

printf "The current release version is $version.\n"
printf "Press [y/n] to proceed: "
read yn
case $yn in
    [Yy]* )
        git add --all
        git commit -v
        git tag $version;;
    * ) exit;;
esac
