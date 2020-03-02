import re   
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import iosxe parser
from genie.libs.parser.iosxe.show_bgp import ShowBgpAllDetail as ShowBgpAllDetail_iosxe,\
                                             ShowBgpAll as ShowBgpAll_iosxe,\
                                             ShowBgpAllSummary as ShowBgpAllSummary_iosxe,\
                                             ShowBgpAllClusterIds as ShowBgpAllClusterIds_iosxe,\
                                             ShowBgpAllNeighbors as ShowBgpAllNeighbors_iosxe, \
                                             ShowIpBgpAllDampeningParameters as ShowIpBgpAllDampeningParameters_iosxe,\
                                             ShowBgpAllNeighborsAdvertisedRoutes as ShowBgpAllNeighborsAdvertisedRoutes_iosxe,\
                                             ShowBgpAllNeighborsRoutes as ShowBgpAllNeighborsRoutes_iosxe,\
                                             ShowBgpAllNeighborsPolicy as ShowBgpAllNeighborsPolicy_iosxe,\
                                             ShowBgpAllNeighborsReceivedRoutes as ShowBgpAllNeighborsReceivedRoutes_iosxe,\
                                             ShowIpBgpTemplatePeerPolicy as ShowIpBgpTemplatePeerPolicy_iosxe,\
                                             ShowIpBgpTemplatePeerSession as ShowIpBgpTemplatePeerSession_iosxe, \
                                             ShowBgpSummary as ShowBgpSummary_iosxe, \
                                             ShowIpBgp as ShowIpBgp_iosxe, \
                                             ShowIpBgpRegexp as ShowIpBgpRegexp_iosxe


from genie.testbed import load
from genie.utils import Dq

tb = load('sandboxtestbed.yaml')
dev = tb.devices['csr1000v-1']
dev.connect()


class ShowIpBgp(ShowIpBgp_iosxe):
    """Parser for show ip bgp"""
    pass


class ShowBgpAllDetail(ShowBgpAllDetail_iosxe):
    """Parser for show bgp all detail"""
    pass


class ShowBgpAllNeighborsPolicy(ShowBgpAllNeighborsPolicy_iosxe):
    """Parser for show bgp all neighbors <neighbor> policy"""
    pass
# ============================================================
# Parser for 'show bgp all neighbors <WORD> advertised-routes'
# ============================================================


class ShowBgpAllNeighborsAdvertisedRoutes(ShowBgpAllNeighborsAdvertisedRoutes_iosxe):
    """Parser for show bgp all neighbors <WORD> advertised-routes"""
    pass

class ShowBgpAllSummary(ShowBgpAllSummary_iosxe):
    """
    Parser for show bgp All Summary
    """
    pass


class ShowBgpAllClusterIds(ShowBgpAllClusterIds_iosxe):
    """
       Parser for show bgp all cluster-ids
       Executing 'show vrf detail | inc \(VRF' to collect vrf names.
    """
    pass


class ShowBgpAllNeighbors(ShowBgpAllNeighbors_iosxe):
    """
    Parser for show bgp all neighbors
    """
    pass


class ShowBgpAllNeighborsReceivedRoutes(ShowBgpAllNeighborsReceivedRoutes_iosxe):

    """
    Parser for show bgp all neighbors <WORD> received-routes
    executing 'show bgp all neighbors | i BGP neighbor' for finging vrf names
    """
    pass

class ShowIpBgpTemplatePeerSession(ShowIpBgpTemplatePeerSession_iosxe):
    """Parser for show ip bgp template peer-session <WORD>"""
    pass

class ShowBgpAllNeighborsRoutes(ShowBgpAllNeighborsRoutes_iosxe):

    """
    Parser for show bgp all neighbors <WORD> routes
    executing 'show bgp all neighbors | i BGP neighbor' for finding vrf names
    """
    pass

class ShowIpBgpTemplatePeerPolicy(ShowIpBgpTemplatePeerPolicy_iosxe):
    """Parser for show ip bgp template peer-policy <WORD>"""
    pass


class ShowIpBgpAllDampeningParameters(ShowIpBgpAllDampeningParameters_iosxe):
    """Parser for show ip bgp all dampening parameters"""
    pass


class ShowBgpAll(ShowBgpAll_iosxe):
    """Parser for show bgp all"""
    pass

class ShowBgpSummary(ShowBgpSummary_iosxe):
    """Parser for show bgp summary"""
    pass

class ShowIpBgpRegexp(ShowIpBgpRegexp_iosxe):
    """Parser for show ip bgp regexp <regexp>"""
    pass