'''
Write a function that when given a URL as a string, parses out just the domain 
name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
'''


# using tldextract
# import tldextract


# def domain_name(url):
#     res = tldextract.extract(url)
#     return res.domain


# without packages


# def domain_name(url):
#     partialDomain = url.split('.')
#     for i in partialDomain:
#         if "www" in i:
#             return partialDomain[1]
#         elif "http" in i:
#             partialDomain.remove(i)
#         elif len(partialDomain) < 3:
#             return partialDomain[0]
#         else:
#             partialDomain = partialDomain[0].split("//")
#             return partialDomain[1]

# attempt #3 working solution

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]

# driver


print(domain_name("https://forums.news.youtube.com"))
