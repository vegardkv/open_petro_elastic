# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["test_grid_model 1"] = GenericRepr(
    "MockGridModel(properties=Properties({'NTG': {frozenset({('realisation', 0)}): array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])}, 'PORO': {frozenset({('realisation', 0)}): array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,\n       0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,\n       0.1])}, 'SWAT_2011': {frozenset({('realisation', 0)}): array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])}, 'SGAS_2011': {frozenset({('realisation', 0)}): array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])}, 'PRESSURE_2011': {frozenset({('realisation', 0)}): array([70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70,\n       70, 70, 70, 70, 70, 70, 70, 70, 70, 70])}, 'RS_2011': {frozenset({('realisation', 0)}): array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])}, 'RV_2011': {frozenset({('realisation', 0)}): array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,\n       0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])}, 'TWTPP_2011': {frozenset({('realisation', 0)}): array([-0.41912308, -0.41912308, -0.41912308,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ])}, 'TWTPS_2011': {frozenset({('realisation', 0)}): array([-0.52467431, -0.52467431, -0.52467431,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ])}, 'TWTSS_2011': {frozenset({('realisation', 0)}): array([-0.63022553, -0.63022553, -0.63022553,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,\n        0.        ,  0.        ])}, 'DTPP_2011': {frozenset({('realisation', 0)}): array([-0.41912308, -0.41912308, -0.41912308, -0.41912308, -0.41912308,\n       -0.41912308, -0.41912308, -0.41912308, -0.41912308, -0.41912308,\n       -0.41912308, -0.41912308, -0.41912308, -0.41912308, -0.41912308,\n       -0.41912308, -0.41912308, -0.41912308, -0.41912308, -0.41912308,\n       -0.41912308, -0.41912308, -0.41912308, -0.41912308, -0.41912308,\n       -0.41912308, -0.41912308])}, 'DTPS_2011': {frozenset({('realisation', 0)}): array([-0.52467431, -0.52467431, -0.52467431, -0.52467431, -0.52467431,\n       -0.52467431, -0.52467431, -0.52467431, -0.52467431, -0.52467431,\n       -0.52467431, -0.52467431, -0.52467431, -0.52467431, -0.52467431,\n       -0.52467431, -0.52467431, -0.52467431, -0.52467431, -0.52467431,\n       -0.52467431, -0.52467431, -0.52467431, -0.52467431, -0.52467431,\n       -0.52467431, -0.52467431])}, 'DTSS_2011': {frozenset({('realisation', 0)}): array([-0.63022553, -0.63022553, -0.63022553, -0.63022553, -0.63022553,\n       -0.63022553, -0.63022553, -0.63022553, -0.63022553, -0.63022553,\n       -0.63022553, -0.63022553, -0.63022553, -0.63022553, -0.63022553,\n       -0.63022553, -0.63022553, -0.63022553, -0.63022553, -0.63022553,\n       -0.63022553, -0.63022553, -0.63022553, -0.63022553, -0.63022553,\n       -0.63022553, -0.63022553])}, 'AI_2011': {frozenset({('realisation', 0)}): array([11764042.30263623, 11764042.30263623, 11764042.30263623,\n       11764042.30263623, 11764042.30263623, 11764042.30263623,\n       11764042.30263623, 11764042.30263623, 11764042.30263623,\n       11764042.30263623, 11764042.30263623, 11764042.30263623,\n       11764042.30263623, 11764042.30263623, 11764042.30263623,\n       11764042.30263623, 11764042.30263623, 11764042.30263623,\n       11764042.30263623, 11764042.30263623, 11764042.30263623,\n       11764042.30263623, 11764042.30263623, 11764042.30263623,\n       11764042.30263623, 11764042.30263623, 11764042.30263623])}, 'SI_2011': {frozenset({('realisation', 0)}): array([7823519.37195199, 7823519.37195199, 7823519.37195199,\n       7823519.37195199, 7823519.37195199, 7823519.37195199,\n       7823519.37195199, 7823519.37195199, 7823519.37195199,\n       7823519.37195199, 7823519.37195199, 7823519.37195199,\n       7823519.37195199, 7823519.37195199, 7823519.37195199,\n       7823519.37195199, 7823519.37195199, 7823519.37195199,\n       7823519.37195199, 7823519.37195199, 7823519.37195199,\n       7823519.37195199, 7823519.37195199, 7823519.37195199,\n       7823519.37195199, 7823519.37195199, 7823519.37195199])}, 'VPVS_2011': {frozenset({('realisation', 0)}): array([1.50367651, 1.50367651, 1.50367651, 1.50367651, 1.50367651,\n       1.50367651, 1.50367651, 1.50367651, 1.50367651, 1.50367651,\n       1.50367651, 1.50367651, 1.50367651, 1.50367651, 1.50367651,\n       1.50367651, 1.50367651, 1.50367651, 1.50367651, 1.50367651,\n       1.50367651, 1.50367651, 1.50367651, 1.50367651, 1.50367651,\n       1.50367651, 1.50367651])}, 'VP_2011': {frozenset({('realisation', 0)}): array([4771.86795324, 4771.86795324, 4771.86795324, 4771.86795324,\n       4771.86795324, 4771.86795324, 4771.86795324, 4771.86795324,\n       4771.86795324, 4771.86795324, 4771.86795324, 4771.86795324,\n       4771.86795324, 4771.86795324, 4771.86795324, 4771.86795324,\n       4771.86795324, 4771.86795324, 4771.86795324, 4771.86795324,\n       4771.86795324, 4771.86795324, 4771.86795324, 4771.86795324,\n       4771.86795324, 4771.86795324, 4771.86795324])}, 'VS_2011': {frozenset({('realisation', 0)}): array([3173.46711378, 3173.46711378, 3173.46711378, 3173.46711378,\n       3173.46711378, 3173.46711378, 3173.46711378, 3173.46711378,\n       3173.46711378, 3173.46711378, 3173.46711378, 3173.46711378,\n       3173.46711378, 3173.46711378, 3173.46711378, 3173.46711378,\n       3173.46711378, 3173.46711378, 3173.46711378, 3173.46711378,\n       3173.46711378, 3173.46711378, 3173.46711378, 3173.46711378,\n       3173.46711378, 3173.46711378, 3173.46711378])}, 'DENS_2011': {frozenset({('realisation', 0)}): array([2465.29082907, 2465.29082907, 2465.29082907, 2465.29082907,\n       2465.29082907, 2465.29082907, 2465.29082907, 2465.29082907,\n       2465.29082907, 2465.29082907, 2465.29082907, 2465.29082907,\n       2465.29082907, 2465.29082907, 2465.29082907, 2465.29082907,\n       2465.29082907, 2465.29082907, 2465.29082907, 2465.29082907,\n       2465.29082907, 2465.29082907, 2465.29082907, 2465.29082907,\n       2465.29082907, 2465.29082907, 2465.29082907])}, 'K_2011': {frozenset({('realisation', 0)}): array([2.30328812e+10, 2.30328812e+10, 2.30328812e+10, 2.30328812e+10,\n       2.30328812e+10, 2.30328812e+10, 2.30328812e+10, 2.30328812e+10,\n       2.30328812e+10, 2.30328812e+10, 2.30328812e+10, 2.30328812e+10,\n       2.30328812e+10, 2.30328812e+10, 2.30328812e+10, 2.30328812e+10,\n       2.30328812e+10, 2.30328812e+10, 2.30328812e+10, 2.30328812e+10,\n       2.30328812e+10, 2.30328812e+10, 2.30328812e+10, 2.30328812e+10,\n       2.30328812e+10, 2.30328812e+10, 2.30328812e+10])}, 'MY_2011': {frozenset({('realisation', 0)}): array([2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10])}, 'RWAT_2011': {frozenset({('realisation', 0)}): array([1008.65351434, 1008.65351434, 1008.65351434, 1008.65351434,\n       1008.65351434, 1008.65351434, 1008.65351434, 1008.65351434,\n       1008.65351434, 1008.65351434, 1008.65351434, 1008.65351434,\n       1008.65351434, 1008.65351434, 1008.65351434, 1008.65351434,\n       1008.65351434, 1008.65351434, 1008.65351434, 1008.65351434,\n       1008.65351434, 1008.65351434, 1008.65351434, 1008.65351434,\n       1008.65351434, 1008.65351434, 1008.65351434])}, 'KWAT_2011': {frozenset({('realisation', 0)}): array([2.62128384e+09, 2.62128384e+09, 2.62128384e+09, 2.62128384e+09,\n       2.62128384e+09, 2.62128384e+09, 2.62128384e+09, 2.62128384e+09,\n       2.62128384e+09, 2.62128384e+09, 2.62128384e+09, 2.62128384e+09,\n       2.62128384e+09, 2.62128384e+09, 2.62128384e+09, 2.62128384e+09,\n       2.62128384e+09, 2.62128384e+09, 2.62128384e+09, 2.62128384e+09,\n       2.62128384e+09, 2.62128384e+09, 2.62128384e+09, 2.62128384e+09,\n       2.62128384e+09, 2.62128384e+09, 2.62128384e+09])}, 'ROIL_2011': {frozenset({('realisation', 0)}): array([802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068])}, 'KOIL_2011': {frozenset({('realisation', 0)}): array([1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09])}, 'RGAS_2011': {frozenset({('realisation', 0)}): array([51.67515387, 51.67515387, 51.67515387, 51.67515387, 51.67515387,\n       51.67515387, 51.67515387, 51.67515387, 51.67515387, 51.67515387,\n       51.67515387, 51.67515387, 51.67515387, 51.67515387, 51.67515387,\n       51.67515387, 51.67515387, 51.67515387, 51.67515387, 51.67515387,\n       51.67515387, 51.67515387, 51.67515387, 51.67515387, 51.67515387,\n       51.67515387, 51.67515387])}, 'KGAS_2011': {frozenset({('realisation', 0)}): array([8292041.46602085, 8292041.46602085, 8292041.46602085,\n       8292041.46602085, 8292041.46602085, 8292041.46602085,\n       8292041.46602085, 8292041.46602085, 8292041.46602085,\n       8292041.46602085, 8292041.46602085, 8292041.46602085,\n       8292041.46602085, 8292041.46602085, 8292041.46602085,\n       8292041.46602085, 8292041.46602085, 8292041.46602085,\n       8292041.46602085, 8292041.46602085, 8292041.46602085,\n       8292041.46602085, 8292041.46602085, 8292041.46602085,\n       8292041.46602085, 8292041.46602085, 8292041.46602085])}, 'RFL_2011': {frozenset({('realisation', 0)}): array([802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068, 802.90829068,\n       802.90829068, 802.90829068, 802.90829068])}, 'KFL_2011': {frozenset({('realisation', 0)}): array([1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09, 1.16847575e+09,\n       1.16847575e+09, 1.16847575e+09, 1.16847575e+09])}, 'RMIN_2011': {frozenset({('realisation', 0)}): array([2650., 2650., 2650., 2650., 2650., 2650., 2650., 2650., 2650.,\n       2650., 2650., 2650., 2650., 2650., 2650., 2650., 2650., 2650.,\n       2650., 2650., 2650., 2650., 2650., 2650., 2650., 2650., 2650.])}, 'KMIN': {frozenset({('realisation', 0)}): array([3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10,\n       3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10,\n       3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10,\n       3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10, 3.68e+10,\n       3.68e+10, 3.68e+10, 3.68e+10])}, 'MYMIN': {frozenset({('realisation', 0)}): array([4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10,\n       4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10,\n       4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10,\n       4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10, 4.4e+10])}, 'VPDRY': {frozenset({('realisation', 0)}): array([4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419])}, 'VSDRY': {frozenset({('realisation', 0)}): array([3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858])}, 'RDRY': {frozenset({('realisation', 0)}): array([2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385.,\n       2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385.,\n       2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385.])}, 'KDRY': {frozenset({('realisation', 0)}): array([2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10])}, 'MYDRY': {frozenset({('realisation', 0)}): array([2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10])}, 'VPDRYREF': {frozenset({('realisation', 0)}): array([4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419])}, 'VSDRYREF': {frozenset({('realisation', 0)}): array([3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858])}, 'RDRYREF': {frozenset({('realisation', 0)}): array([2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385.,\n       2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385.,\n       2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385.])}, 'KDRYREF': {frozenset({('realisation', 0)}): array([2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10])}, 'MYDRYREF': {frozenset({('realisation', 0)}): array([2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10])}, 'VPDRYPHI': {frozenset({('realisation', 0)}): array([4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419, 4767.60987419,\n       4767.60987419, 4767.60987419, 4767.60987419])}, 'VSDRYPHI': {frozenset({('realisation', 0)}): array([3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858, 3226.44220858,\n       3226.44220858, 3226.44220858, 3226.44220858])}, 'RDRYPHI': {frozenset({('realisation', 0)}): array([2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385.,\n       2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385.,\n       2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385., 2385.])}, 'KDRYPHI': {frozenset({('realisation', 0)}): array([2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10, 2.11077226e+10,\n       2.11077226e+10, 2.11077226e+10, 2.11077226e+10])}, 'MYDRYPHI': {frozenset({('realisation', 0)}): array([2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10, 2.48276814e+10,\n       2.48276814e+10, 2.48276814e+10, 2.48276814e+10])}}), grid=MockGrid(grid_indexer=MockGridIndexer(dimensions=(3, 3, 3))))"
)
