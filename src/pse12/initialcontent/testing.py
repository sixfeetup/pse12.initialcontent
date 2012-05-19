from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class Pse12Initialcontent(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import pse12.initialcontent
        xmlconfig.file('configure.zcml',
                       pse12.initialcontent,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'pse12.initialcontent:default')

PSE12_INITIALCONTENT_FIXTURE = Pse12Initialcontent()
PSE12_INITIALCONTENT_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(PSE12_INITIALCONTENT_FIXTURE, ),
                       name="Pse12Initialcontent:Integration")