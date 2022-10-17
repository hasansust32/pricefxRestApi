#
# # import csv
# #
# # with open("DataSet/ProductMappingData.csv", 'r') as file:
# #   csvreader = csv.reader(file)
# #   for row in csvreader:
# #     print(row)
#
#
#
# # import sys
# # import trace
# # import csv
# #
# # with open("DataSet/ProductMappingData.csv", 'r') as file:
# #   csvreader = csv.reader(file)
# #   for row in csvreader:
# #       productMap = {
# #           row[0] : row[1]
# #       }
# #       print(productMap)
# # tracer = trace.Trace(
# #     ignoredirs=[sys.prefix, sys.exec_prefix],
# #     trace=0,
# #     count=1)
# # # tracer.run('productMap.py')
# # r = tracer.results()
# # r.write_results(show_missing=True, coverdir=".")
#
#
#
#
# import csv
#
# with open("DataSet/ProductMappingData.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   for row in csvreader:
#       productMap = {
#           row[0] : row[1]
#       }
#       # print(productMap)
#       print(productMap)
#


def Migration():
    import csv

    with open("DataSet/ProductMappingData.csv", 'r') as file:
        csvreader = csv.reader(file)
        Migration = {

        }

        for row in csvreader:
            Migration[row[0]] = row[1]

        return (Migration)


print(Migration())

