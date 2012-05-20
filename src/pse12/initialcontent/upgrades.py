from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName
from sixfeetup.utils import helpers as sfutils


def intranet_setup(context):
    """Set up the placeful workflow for the intranet
    """
    portal = getSite()
    # If the intranet doesn't exist, bail out
    if 'intranet' not in portal.objectIds():
        return
    intranet = portal['intranet']
    # If the placeful workflow is already in place, bail out
    if '.wf_policy_config' in intranet.objectIds():
        return
    placeful_workflow = getToolByName(portal, 'portal_placeful_workflow')
    product = 'CMFPlacefulWorkflow'
    intranet.manage_addProduct[product].manage_addWorkflowPolicyConfig()
    config = placeful_workflow.getWorkflowPolicyConfig(intranet)
    policy = 'intranet'
    config.setPolicyBelow(policy=policy)
    config.setPolicyIn(policy=policy)
    # Make everything in the intranet `private`
    path = '/'.join(intranet.getPhysicalPath())
    sfutils.publishEverything(context, path, 'hide')


def default_pages(context):
    """There is a bug in quintagroup.transmogrifier that prevents
    the default page from being set. We will handle it here
    instead.
    """
    portal = getSite()
    items = {
        'news-events': dict(
            id='default_page',
            type='string',
            value='what-are-we-up-to'),
        'news-events/events': dict(
            id='default_page',
            type='string',
            value='events'),
    }
    for path, prop in items.items():
        obj = portal.unrestrictedTravers(path, None)
        # If the object doesn't exist, bail out
        if obj is None:
            continue
        obj._setProperty(prop['id'], prop['value'], prop['value'])
