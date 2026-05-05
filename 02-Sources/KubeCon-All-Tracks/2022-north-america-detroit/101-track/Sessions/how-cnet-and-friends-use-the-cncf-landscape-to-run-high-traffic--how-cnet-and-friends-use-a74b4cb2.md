---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "101 Track"
themes: ["SRE Reliability"]
speakers: ["Corey McGalliard", "Red Ventures"]
sched_url: https://kccncna2022.sched.com/event/182F4/how-cnet-and-friends-use-the-cncf-landscape-to-run-high-traffic-dynamic-scalable-and-cost-effective-websites-corey-mcgalliard-red-ventures
youtube_search_url: https://www.youtube.com/results?search_query=How+CNET+%28And+Friends%29+Use+the+CNCF+Landscape+To+Run+High+Traffic%2C+Dynamic%2C+Scalable%2C+And+Cost-Effective+Websites.+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How CNET (And Friends) Use the CNCF Landscape To Run High Traffic, Dynamic, Scalable, And Cost-Effective Websites. - Corey McGalliard, Red Ventures

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[101 Track]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Corey McGalliard, Red Ventures
- Schedule: https://kccncna2022.sched.com/event/182F4/how-cnet-and-friends-use-the-cncf-landscape-to-run-high-traffic-dynamic-scalable-and-cost-effective-websites-corey-mcgalliard-red-ventures
- Busca YouTube: https://www.youtube.com/results?search_query=How+CNET+%28And+Friends%29+Use+the+CNCF+Landscape+To+Run+High+Traffic%2C+Dynamic%2C+Scalable%2C+And+Cost-Effective+Websites.+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How CNET (And Friends) Use the CNCF Landscape To Run High Traffic, Dynamic, Scalable, And Cost-Effective Websites..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182F4/how-cnet-and-friends-use-the-cncf-landscape-to-run-high-traffic-dynamic-scalable-and-cost-effective-websites-corey-mcgalliard-red-ventures
- YouTube search: https://www.youtube.com/results?search_query=How+CNET+%28And+Friends%29+Use+the+CNCF+Landscape+To+Run+High+Traffic%2C+Dynamic%2C+Scalable%2C+And+Cost-Effective+Websites.+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pzyid-_2cY0
- YouTube title: How CNET (And Friends) Use the CNCF Landscape To Run High Traffic, Dynamic... - Corey McGalliard
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-cnet-and-friends-use-the-cncf-landscape-to-run-high-traffic-dynami/pzyid-_2cY0.txt
- Transcript chars: 31044
- Keywords: manager, traffic, ingress, google, external, actually, cluster, change, workload, containers, certificate, running, inside, production, request, probably, managed, engineers

### Resumo baseado na transcript

hey thanks for coming to my talk um I try to go for the longest title award I think this year uh how I've seen that in friends use cncf landscape to run high traffic Dynamic uh scalable cost-effective websites um also just went for all those great bud buzzwords right my name is Corey McGalliard I'm an engineering manager for a company called Red Ventures probably the largest Media Company you've never heard of uh we haven't seen that but also quite a few other large websites you can

### Excerpt da transcript

hey thanks for coming to my talk um I try to go for the longest title award I think this year uh how I've seen that in friends use cncf landscape to run high traffic Dynamic uh scalable cost-effective websites um also just went for all those great bud buzzwords right my name is Corey McGalliard I'm an engineering manager for a company called Red Ventures probably the largest Media Company you've never heard of uh we haven't seen that but also quite a few other large websites you can go check out the website later to learn about us but um but I've been with CNET specifically for about three three and a half years now um and seeing that's been around for a while it started in 1994. I was originally a Ted network not a lot of people actually realized that we started with the focus on TV and then shifted to a web presence afterwards we see about 45 billion requests monthly at Edge and uh 10 billion requests at origin per second which is probably a metric we're more comfortable with that's 20 000 requests a second and five to ten depending on the metric you look at down to the actual containers at origin right um CNET has a rather long history of acquisition so starting in 94 they started gobbling up Brands and then was purchased by CBS Interactive in 2008 and then when I joined CBS Interactive in 2009 they were being a choir sorry 2019 they were being acquired by Viacom and then we were sold to Red Ventures a year after that um we also have quite a bit of Technology leadership um over the years CNET because we've been around right and have developed stuff we actually developed solar the search index and that was donated to Apache we also were active with mood tools and then we adopted Docker and Docker swarm actually really really early I've seen references back to 2015 2016 era uh when when that started to kind of take take shape and then also we have uh the links are here for most of these are either talks or documents about the history but we've been pretty open about our Google Cloud migration over the last three years um so why kubernetes right so this is a talk to really kind of talk about why we made the decision as an organization to move from Docker swarm to kubernetes um we started about two and a half three years ago really initiating the the the the process of doing this and the first few things I think everybody will like agree with these things they're really comfortable with we see it is super flexible platform has all this all these tools avail
