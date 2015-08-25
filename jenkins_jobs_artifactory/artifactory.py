import xml.etree.ElementTree as XML


def artifactory_wrapper(parser, xml_parent, data):
        """yaml: artifactory

        Example::

            properties:
                - artifactory:
                        artifactory-name: "yyyyy@xxxxxxxx"
                        artifactory-repository-key: "repo-name"
                        artifactory-snapshot-repository-key: "repo-name"
                        artifactory-url: "URL"
                        artifactory-deploy-pattern: "*.rpm"
                        artifactory-deploy-buildinfo: true
                        artifactory-include-envvars: true
                        artifactory-exclude-patterns: "*password*,*secret*"
                        artifactory-discard-oldbuilds: false
                        artifactory-discard-buildartifacts: true
                        artifactory-multiconf: false
        """
        if data is None:
          data = dict()

        notifier = XML.SubElement(xml_parent,'org.jfrog.hudson.generic.ArtifactoryGenericConfigurator')
        notifier.set('plugin','artifactory@2.2.7')

        details = XML.SubElement(notifier, 'details')

        for opt, attr in (('artifactory-name', 'artifactoryName'),
                                            ('artifactory-repository-key', 'repositoryKey'),
                                            ('artifactory-snapshot-repository-key', 'snapshotsRepositoryKey'),
                                            ('artifactory-url', 'artifactoryUrl'),
                                            ('artifactory-staging','stagingPlugin')):
          XML.SubElement(details, attr).text = data.get(opt, '')

        for opt, attr in (('artifactory-deploy-pattern', 'deployPattern'),
                                            ('artifactory-resolve-pattern','resolvePattern'),
                                            ('artifactory-matrix-params','matrixParams'),
                                            ('artifactory-deploy-buildinfo','deployBuildInfo'),
                                            ('artifactory-include-envvars', 'includeEnvVars')):
          XML.SubElement(notifier, attr).text = data.get(opt, '')


        envpatterns = XML.SubElement(notifier, 'envVarsPatterns')

        for opt, attr in (('artifactory-include-patterns', 'includePatterns'),
                                            ('artifactory-exclude-patterns', 'excludePatterns')):
          XML.SubElement(envpatterns, attr).text = data.get(opt, '')

        for opt, attr in (('artifactory-discard-oldbuilds', 'discardOldBuilds'),
                                            ('artifactory-discard-buildartifacts', 'discardBuildArtifacts'),
                                            ('artifactory-multiconf', 'multiConfProject')):
          XML.SubElement(notifier, attr).text = data.get(opt, '')

def artifactory_publisher(parser, xml_parent, data):
        """yaml: artifactory

        Example::

            publishers:
                - artifactory:
                        artifactory-name: "yyyyy@xxxxxxxx"
                        artifactory-repository-key: "repo-name"
                        artifactory-snapshot-repository-key: "repo-name"
                        artifactory-url: "URL"
                        artifactory-deploy-artifacts: true
                        artifactory-include-artifacts: "*.rpm"
                        artifactory-deploy-buildinfo: true
                        artifactory-include-envvars: true
                        artifactory-exclude-patterns: "*password*,*secret*"
                        artifactory-discard-oldbuilds: false
                        artifactory-discard-buildartifacts: true
                        artifactory-multiconf: false
        """
        if data is None:
          data = dict()

        notifier = XML.SubElement(xml_parent,'org.jfrog.hudson.ArtifactoryRedeployPublisher')
        notifier.set('plugin','artifactory@2.2.7')

        details = XML.SubElement(notifier, 'details')

        for opt, attr in (('artifactory-name', 'artifactoryName'),
                                            ('artifactory-repository-key', 'repositoryKey'),
                                            ('artifactory-snapshot-repository-key', 'snapshotsRepositoryKey'),
                                            ('artifactory-url', 'artifactoryUrl'),
                                            ('artifactory-staging','stagingPlugin')):
          XML.SubElement(details, attr).text = data.get(opt, '')

        for opt, attr in (('artifactory-resolve-pattern','resolvePattern'),
                                            ('artifactory-matrix-params','matrixParams'),
                                            ('artifactory-deploy-buildinfo','deployBuildInfo'),
                                            ('artifactory-deploy-artifacts','deployArtifacts'),
                                            ('artifactory-include-envvars', 'includeEnvVars')):
          XML.SubElement(notifier, attr).text = data.get(opt, '')

        artifactspatterns = XML.SubElement(notifier, 'artifactDeploymentPatterns')

        for opt, attr in (('artifactory-include-artifacts', 'includePatterns'),
                                            ('artifactory-exclude-artifacts', 'excludePatterns')):
          XML.SubElement(artifactspatterns, attr).text = data.get(opt, '')

        envpatterns = XML.SubElement(notifier, 'envVarsPatterns')

        for opt, attr in (('artifactory-include-patterns', 'includePatterns'),
                                            ('artifactory-exclude-patterns', 'excludePatterns')):
          XML.SubElement(envpatterns, attr).text = data.get(opt, '')

        for opt, attr in (('artifactory-discard-oldbuilds', 'discardOldBuilds'),
                                            ('artifactory-discard-buildartifacts', 'discardBuildArtifacts'),
                                            ('artifactory-multiconf', 'multiConfProject')):
          XML.SubElement(notifier, attr).text = data.get(opt, '')
