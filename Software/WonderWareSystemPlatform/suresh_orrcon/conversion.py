from Software.WonderWareSystemPlatform.GalaxyDump.galaxydata import GalaxyData as GD
import pandas as pd


def main():

    gd = GD()

    print(gd.dataframe_dict)
    print('-'*30)


    for template, data in gd.dataframe_dict.items():
        print(template)

        groups = {}

        for key, val in data.iteritems():

            if '.' in key:

                key_split = key.split('.', 1)

                if key_split[0] not in groups:

                    groups[key_split[0]] = []

                groups[key_split[0]].append({key_split[-1]: val})



    # convert groups to dfs

    dfs = []

    for group_key, group_val in groups.items():

        # generate df
        df = pd.DataFrame()

        df[':Tagname'] = [f'{s}.{group_key}' for s in list(gd.dataframe_dict.values())[0][':Tagname']]

        for col_data in group_val:

            for sub_key, sub_val in col_data.items():

                df[sub_key] = sub_val

        dfs.append(df)

    print(pd.concat(dfs).to_excel('example_output.xlsx'))


if __name__ == '__main__':

    main()
