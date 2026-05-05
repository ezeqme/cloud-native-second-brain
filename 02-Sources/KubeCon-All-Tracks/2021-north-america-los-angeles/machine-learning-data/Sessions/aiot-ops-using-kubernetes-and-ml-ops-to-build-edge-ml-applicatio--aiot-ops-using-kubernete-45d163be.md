---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Asheesh Goja", "Cisco"]
sched_url: https://kccncna2021.sched.com/event/lV3G/aiot-ops-using-kubernetes-and-ml-ops-to-build-edge-ml-applications-asheesh-goja-cisco
youtube_search_url: https://www.youtube.com/results?search_query=AIoT+Ops+-+Using+Kubernetes+and+ML+Ops+to+Build+Edge+ML+Applications+CNCF+KubeCon+2021
slides: []
status: parsed
---

# AIoT Ops - Using Kubernetes and ML Ops to Build Edge ML Applications - Asheesh Goja, Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Asheesh Goja, Cisco
- Schedule: https://kccncna2021.sched.com/event/lV3G/aiot-ops-using-kubernetes-and-ml-ops-to-build-edge-ml-applications-asheesh-goja-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=AIoT+Ops+-+Using+Kubernetes+and+ML+Ops+to+Build+Edge+ML+Applications+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre AIoT Ops - Using Kubernetes and ML Ops to Build Edge ML Applications.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV3G/aiot-ops-using-kubernetes-and-ml-ops-to-build-edge-ml-applications-asheesh-goja-cisco
- YouTube search: https://www.youtube.com/results?search_query=AIoT+Ops+-+Using+Kubernetes+and+ML+Ops+to+Build+Edge+ML+Applications+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uJ-rGoXICaY
- YouTube title: AIoT Ops - Using Kubernetes and ML Ops to Build Edge ML Applications - Asheesh Goja, Cisco
- Match score: 0.954
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/aiot-ops-using-kubernetes-and-ml-ops-to-build-edge-ml-applications/uJ-rGoXICaY.txt
- Transcript chars: 31058
- Keywords: devices, running, training, device, inference, machine, learning, cluster, architecture, reference, hardware, pipelines, message, particular, container, question, libraries, analog

### Resumo baseado na transcript

hello everyone and welcome to my talk i hope you had a good sessions in the keynotes this morning and now uh i'm happy to take you on a journey from the world of cloud native computing to the world of edge computing and in this journey we will learn how kubernetes can be used to control and manage aiot machine learning pipelines on the edge devices a little bit about me i am i work as a solutions architect in one of the best teams within cisco called emerging

### Excerpt da transcript

hello everyone and welcome to my talk i hope you had a good sessions in the keynotes this morning and now uh i'm happy to take you on a journey from the world of cloud native computing to the world of edge computing and in this journey we will learn how kubernetes can be used to control and manage aiot machine learning pipelines on the edge devices a little bit about me i am i work as a solutions architect in one of the best teams within cisco called emerging technologies and incubation my talk today has two sections i will first talk about why aiot what is important about it and when we bring a i and ml together what are the emergent behaviors uh what are the patterns that help us solve those behaviors and i'll also show you a comprehensive reference architecture on how to build an aiotml solution along with the reference implementation and then a live demo the demo is the most interesting part i had a lot of fun building all this hardware i spent many weeks do it three hours and you know sleep but i will share all the journey with you and this is one of the reasons why i was able to come up with a reference architecture the lessons learned in the journey of building this demo is what shows up in the reference architecture so what is what is aiot we all know and have heard that the number of internet connected devices is growing each year most industry analysts say that by year in next three years we will have close to 55 billion devices but that's where we reach a point of diminishing returns what we find is the more devices we get in the correct internet the less insights we're getting and at the same time we're also seeing that as these devices and they connect to the internet the cyber security attack vectors keep increasing progressively so what is the solution the solution lies in looking closely at what do the devices do when they connect internet their primary reason to connect the internet is to push the data to the cloud tier so that we can generate insights and power our business applications and there analyze the solution what if that the power of making insights and inferences is brought down closer to these embedded devices but that's easier said than done once we do that there are a lot of problems that arise in in putting them together and that's what i'm going to talk about in the emerging behaviors the first thing that we see is as soon as we start to think about bringing machine learning to edge devices or embedded devices is the comput
