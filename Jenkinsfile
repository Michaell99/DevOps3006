properties([pipelineTriggers([pollSCM('* * * * *')])])
node{
    stage("clone"){
     git"https://github.com/Michaell99/DevOps3006.git"
    }
    stage("show files"){
        bat "dir"
    }
}
