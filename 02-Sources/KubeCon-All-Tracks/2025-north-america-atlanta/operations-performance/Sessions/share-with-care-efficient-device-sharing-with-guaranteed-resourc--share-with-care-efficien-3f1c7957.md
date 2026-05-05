---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Sunyanan Choochotkaew", "IBM Research", "John Belamaric", "Google"]
sched_url: https://kccncna2025.sched.com/event/27FWB/share-with-care-efficient-device-sharing-with-guaranteed-resources-using-dra-sunyanan-choochotkaew-ibm-research-john-belamaric-google
youtube_search_url: https://www.youtube.com/results?search_query=Share+With+Care%3A+Efficient+Device+Sharing+With+Guaranteed+Resources+Using+DRA+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Share With Care: Efficient Device Sharing With Guaranteed Resources Using DRA - Sunyanan Choochotkaew, IBM Research & John Belamaric, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Sunyanan Choochotkaew, IBM Research, John Belamaric, Google
- Schedule: https://kccncna2025.sched.com/event/27FWB/share-with-care-efficient-device-sharing-with-guaranteed-resources-using-dra-sunyanan-choochotkaew-ibm-research-john-belamaric-google
- Busca YouTube: https://www.youtube.com/results?search_query=Share+With+Care%3A+Efficient+Device+Sharing+With+Guaranteed+Resources+Using+DRA+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Share With Care: Efficient Device Sharing With Guaranteed Resources Using DRA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWB/share-with-care-efficient-device-sharing-with-guaranteed-resources-using-dra-sunyanan-choochotkaew-ibm-research-john-belamaric-google
- YouTube search: https://www.youtube.com/results?search_query=Share+With+Care%3A+Efficient+Device+Sharing+With+Guaranteed+Resources+Using+DRA+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=L1NRskjrvDo
- YouTube title: Share With Care: Efficient Device Sharing With Guaranteed... Sunyanan Choochotkaew & John Belamaric
- Match score: 0.778
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/share-with-care-efficient-device-sharing-with-guaranteed-resources-usi/L1NRskjrvDo.txt
- Transcript chars: 27063
- Keywords: device, bandwidth, resource, capacity, multiple, feature, request, gpu, network, secondary, second, inside, minimum, actually, memory, devices, resources, allocated

### Resumo baseado na transcript

Um, and, uh, I've been working, uh, in upstream Kubernetes for a while now, and we wanted to share with you some of the really early things, but this is an alpha feature, but like we want to show you some of the interesting things we're working on and my co-speaker here. Um, so I guess I should have done this slide while I talked about that, but um, so what we're going to talk a little bit about is a use case that Kubernetes uh, people have been doing on Kubernetes for a while, but really has been challenging for a number of reasons. Now the problem with this is that theuler has zero visibility into those annotations. Um, Kubernetes has a feature called extended resources and in extended resources you can go into a node and you can say hey actually this node has um a bandwidth resource and it's got 10 gigs of bandwidth on on that node and uh the And now you're getting really bespoke like configurations between your nodes and your pods and it's really hard to scale and you know it it's just extremely awkward. Now, so kind of to give the very high level overview and and if you want to learn more about DRA, there's a another talk later today around I think it's at 4:15 is it 4:30?

### Excerpt da transcript

All right. Hello everybody. Um, hope you're doing well today. Uh, my name is John Bellame. Um, and, uh, I've been working, uh, in upstream Kubernetes for a while now, and we wanted to share with you some of the really early things, but this is an alpha feature, but like we want to show you some of the interesting things we're working on and my co-speaker here. >> Hi. Uh, I'm Syan. I'm working for IBM research. My research area is networking performance optimizations. And this year is my first time to contribute it to the Kubernetes. >> Yes, thank you. Um, so I guess I should have done this slide while I talked about that, but um, so what we're going to talk a little bit about is a use case that Kubernetes uh, people have been doing on Kubernetes for a while, but really has been challenging for a number of reasons. So, um, to kind of set up the the story, uh, imagine that imagine that you're, uh, you've got a network service. And so, with this network service, there's a few different components you have in it.

And, uh, you really need, you know, this is a streaming service. So, you really need to have guaranteed bandwidth for your users to be able to get smooth streaming, uh, from from your service. So these different three different components are running in three different pods and um they have some uh very specific network uh requirements. So what you would do today in Kubernetes is you might use uh a special CNI uh in order to manage the bandwidth allocated to those on your secondary nicks. So you wouldn't be using the necessarily the cluster the cluster nick for this. You might be using a secondary nick for it, but you want to use that and divide up the bandwidth. Um so as an example you could use a you know put some annotations on your pod and uh you you can uh guarantee the bandwidth to each each pod on that nick. Now the problem with this is that theuler has zero visibility into those annotations. Um, and so what can happen is that if you've got a 10 Gbit nick and your different services in combination may exceed those that 10 Gbits, the scheduler will simply schedule them there anyway and so you end up um running out of bandwidth uh and your users have a poor experience.

Um so how do how do we solve that? Um, Kubernetes has a feature called extended resources and in extended resources you can go into a node and you can say hey actually this node has um a bandwidth resource and it's got 10 gigs of bandwidth on on that node and uh the scheduler the
