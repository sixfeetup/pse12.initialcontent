from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName


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
    wftool = getToolByName(portal, 'portal_workflow')
    product = 'CMFPlacefulWorkflow'
    intranet.manage_addProduct[product].manage_addWorkflowPolicyConfig()
    config = placeful_workflow.getWorkflowPolicyConfig(intranet)
    policy = 'intranet'
    config.setPolicyBelow(policy=policy)
    config.setPolicyIn(policy=policy)
    wftool.doActionFor(intranet, 'hide')
