jenkins-jobs-artifactory
==================

Artifactory integration with jenkins job builder using the generic integration at the moment.

# How to use/extend?

If there is any extra thing you want to add or you want to see what values jenkins is putting in the fields, do the following.Manually configure a jenkins job to enable artifactory integration and add the values you want. Then visit the JOB url by adding a config.xml at the end to get the config for the job in XML.It should be like that 

```
<buildWrappers>
<org.jfrog.hudson.generic.ArtifactoryGenericConfigurator plugin="artifactory@2.2.7">
<details>
<artifactoryName>xxxxxxxx</artifactoryName>
<repositoryKey>xxxxxxxxx</repositoryKey>
<snapshotsRepositoryKey>xxxxxxxxxx</snapshotsRepositoryKey>
<artifactoryUrl>xxxxxxxxxxx</artifactoryUrl>
<stagingPlugin/>
</details>
<deployPattern>*.rpm</deployPattern>
<resolvePattern/>
<matrixParams/>
<deployBuildInfo>true</deployBuildInfo>
<includeEnvVars>true</includeEnvVars>
<envVarsPatterns>
<includePatterns/>
<excludePatterns>*password*,*secret*</excludePatterns>
</envVarsPatterns>
<discardOldBuilds>false</discardOldBuilds>
<discardBuildArtifacts>true</discardBuildArtifacts>
<multiConfProject>false</multiConfProject>
</org.jfrog.hudson.generic.ArtifactoryGenericConfigurator>
```

If something is missing add it in the artifactory.py or modify it to cover more use cases.Then having a yaml job with the following will work:

```
JOB123:
    delay: 120
    config:
      - job:
          name: "xxxxxx"
          workspace: "xxxxx"
          description: "xxxxxxx"
          project-type: freestyle
          auth-token: "xxxxxx"
          builders:
            - shell: |
                lalalalallalaalalal
          wrappers:
            - artifactory:
               artifactory-name: "xxxx"
               artifactory-repository-key: "xxxxx"
               artifactory-snapshot-repository-key: "xxxxx"
               artifactory-url: "xxxxx"
               artifactory-deploy-pattern: "*.rpm"
               artifactory-deploy-buildinfo: "true"
               artifactory-include-envvars: "true"
               artifactory-exclude-patterns: "*password*,*secret*"
               artifactory-discard-oldbuilds: "false"
               artifactory-discard-buildartifacts: "true"
               artifactory-multiconf: "false"
               
```

# Use with puppet
```
 package{ 'jenkins-jobs-artifactory':
    provider => 'pip',
    source   => 'git+https://github.com/xiii/jenkins-jobs-artifactory'
  }
```

# Problems & TODO

This is locked at the moment to version of 2.2.7 of jenkins artifactory. I need to make the version a variable.
