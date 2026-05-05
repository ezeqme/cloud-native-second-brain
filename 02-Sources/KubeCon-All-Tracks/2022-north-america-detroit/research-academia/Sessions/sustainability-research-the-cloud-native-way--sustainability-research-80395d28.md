---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Research + Academia"
themes: ["AI ML", "Sustainability"]
speakers: ["Chen Wang", "IBM", "Huamin Chen", "Red Hat"]
sched_url: https://kccncna2022.sched.com/event/182JN/sustainability-research-the-cloud-native-way-chen-wang-ibm-huamin-chen-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Sustainability+Research+the+Cloud+Native+Way+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Sustainability Research the Cloud Native Way - Chen Wang, IBM & Huamin Chen, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Research + Academia]]
- Temas: [[AI ML]], [[Sustainability]]
- País/cidade: United States / Detroit
- Speakers: Chen Wang, IBM, Huamin Chen, Red Hat
- Schedule: https://kccncna2022.sched.com/event/182JN/sustainability-research-the-cloud-native-way-chen-wang-ibm-huamin-chen-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Sustainability+Research+the+Cloud+Native+Way+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Sustainability Research the Cloud Native Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182JN/sustainability-research-the-cloud-native-way-chen-wang-ibm-huamin-chen-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Sustainability+Research+the+Cloud+Native+Way+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dfGSqhAZ2qo
- YouTube title: Sustainability Research the Cloud Native Way - Chen Wang, IBM & Huamin Chen, Red Hat
- Match score: 0.801
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/sustainability-research-the-cloud-native-way/dfGSqhAZ2qo.txt
- Transcript chars: 26196
- Keywords: workload, energy, frequency, clever, kepler, recommender, metrics, performance, workloads, frequencies, running, information, capital, cluster, account, projects, current, guarantee

### Resumo baseado na transcript

thank you thank you Sean for the introduction and it's my pleasure to meet you all and let's celebrate for this afternoon and with some of the good ideas and the introductions of what we have done for sustainability and for the research community and so if you I just want to put a certain words and certain criterias of what we do and what we see is cloud native sustainability Republican using a few characters some colors to paint the picture so I call it IMC coupe not to ipis over time this is how clever utilizing the Kepler metrics to guarantee you have the same performance as well as saving some energy okay so uh looking forward uh we will try to enhance the whole Kepler uh project with uh some carbon footprint

### Excerpt da transcript

thank you thank you Sean for the introduction and it's my pleasure to meet you all and let's celebrate for this afternoon and with some of the good ideas and the introductions of what we have done for sustainability and for the research community and so if you I just want to put a certain words and certain criterias of what we do and what we see is cloud native sustainability Republican using a few characters some colors to paint the picture so I call it IMC coupe not to understand not too confused with mcsquare so for m i mean metrics so as we um many of you have noticed for cloud native its observability that gives us a lot of power for scheduling for scale for scaling and for a lot of management and costs and availability so having enough mess with metrics will give you the insights into what we what we can do so the metrics we build is for energy conservation so specifically we want to know how much energy consumed by a workloads in Cloud native in kubernetes that means the part level how much energy you use by the node by the parts the second is one we call correlation so having this Matrix makes sense to end user but start not making use for the end user in terms of doing the energy conservation so when you schedule a workloads how do you correlate with the metrics with the hardware characteristics such as the scheduling of your workloads will be optimized for energy consumption so after the scheduling the workloads landed on the nodes it keeps running for days and weeks and even for months if signage of the original assumption about the resource consumption resource assignments goes wrong how do you correct this runtime Behavior so we call this the correction phase in this phase we use an auto scaling capabilities in the kubernetes community as very last one once you go beyond a single cluster you want to take into account of the carbon Deltas Around the World abusing different clusters that is about the multi-clusters use case comes in and we want to account for the carbon intensity differences in between multiple clusters and find the best attest animations for your workloads to land on um let's come down to the projects we are trying to uh the problem with our project is trying to address the projects in other problems in the cloud native power management system first of all you want to have accuracy right accuracy means there are metrics we presented to you about the part about the containers as accurate as we can see everybody will agree on the
