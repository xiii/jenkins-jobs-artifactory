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

    notifier = XML.SubElement(
        xml_parent, 'org.jfrog.hudson.generic.ArtifactoryGenericConfigurator')
    notifier.set('plugin', 'artifactory@2.2.7')

    for opt, attr in (('artifactory-name', 'artifactoryName'),
                      ('artifactory-repository-key', 'repositoryKey'),
                      ('artifactory-snapshot-repository-key', 'snapshotsRepositoryKey'),
                      ('artifactory-url', 'artifactoryUrl'),
                      ('artifactory-deploy-pattern', 'deployPattern'),
                      ('artifactory-deploy-buildinfo','deployBuildInfo'),
                      ('artifactory-include-envvars', 'includeEnvVars'),
                      ('artifactory-exclude-patterns', 'excludePatterns'),
                      ('artifactory-discard-oldbuilds', 'discardOldBuilds'),
                      ('artifactory-discard-buildartifacts', 'discardBuildArtifacts'),
                      ('artifactory-multiconf', 'multiConfProject')):
        XML.SubElement(notifier, attr).text = data.get(opt, '')