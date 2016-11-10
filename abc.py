TARGET_OVERRIDES = ('EE_GATEWAY_IT','BSKYB_GATEWAY_WB')
for each in TARGET_OVERRIDES:
        TARGET_VARS[each] = {
                'FUSION_SGW_SERVER_NAME': "bskyb-dms-sgw-in.in.nds.com",
                'FUSION_SGW_SERVER_ADDRESS': "10.197.109.99",
                'FUSION_SGW_SERVER_PORT': "6007,"
                }

