---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Data Processing + Storage"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Florian Coulombel", "Dell Technologies", "Jan Šafránek", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1i7q7/kubernetes-on-multisites-a-story-about-stateful-app-hybrid-clouds-and-high-availability-florian-coulombel-dell-technologies-jan-safranek-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+on+Multisites+%E2%80%93+A+Story+About+Stateful+App%2C+Hybrid+Clouds%2C+and+High+Availability+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes on Multisites – A Story About Stateful App, Hybrid Clouds, and High Availability - Florian Coulombel, Dell Technologies & Jan Šafránek, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Florian Coulombel, Dell Technologies, Jan Šafránek, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1i7q7/kubernetes-on-multisites-a-story-about-stateful-app-hybrid-clouds-and-high-availability-florian-coulombel-dell-technologies-jan-safranek-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+on+Multisites+%E2%80%93+A+Story+About+Stateful+App%2C+Hybrid+Clouds%2C+and+High+Availability+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes on Multisites – A Story About Stateful App, Hybrid Clouds, and High Availability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7q7/kubernetes-on-multisites-a-story-about-stateful-app-hybrid-clouds-and-high-availability-florian-coulombel-dell-technologies-jan-safranek-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+on+Multisites+%E2%80%93+A+Story+About+Stateful+App%2C+Hybrid+Clouds%2C+and+High+Availability+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BaLVmNYDxO8
- YouTube title: Kubernetes on Multisites – A Story About Stateful App, Hybrid Clouds, a... F. Coulombel, J. Šafránek
- Match score: 0.875
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-on-multisites-a-story-about-stateful-app-hybrid-clouds-and/BaLVmNYDxO8.txt
- Transcript chars: 20325
- Keywords: storage, cluster, application, volume, replication, virtual, elastic, availability, usually, multiple, active, within, little, basically, spread, running, topology, infrastructure

### Resumo baseado na transcript

all right hey Cube conon dayre do you still have some [Music] energy wo thank you for being here um yeah yes last night I was at the Jazz game TI until the last second so yeah I hope we can uh share some good knowledge with you till the last time so our topic today is about kubernetes on Multi sight but it's really about designing application and Cube infrastructure so it's highly a able and resilient so before we begin I have a a small quiz for you

### Excerpt da transcript

all right hey Cube conon dayre do you still have some [Music] energy wo thank you for being here um yeah yes last night I was at the Jazz game TI until the last second so yeah I hope we can uh share some good knowledge with you till the last time so our topic today is about kubernetes on Multi sight but it's really about designing application and Cube infrastructure so it's highly a able and resilient so before we begin I have a a small quiz for you does anybody know about these little characters I guess there is no French in the room so there is one oh really so these are uh little people who live on the other planets and uh what they do all day is pumping to solve issues and one of their Mantra is why making it simple when it can be complex and dealing with Cube quite often I I have that feeling so I'm Flor working for Del Technologies in the product management team for every devops um we do at down I am Yan shafran I work at redhead on open shift storage and I am a sick storage T Tech Upstream so our main goal today will be to as much as possible make kuber on Multi side concept simple when it can be complicated sometimes so so first why am I talking to you about this kubernetes on Multi sites and working on this presentation basically I found that maybe it was the wrong the wrong title it's really about designing app designing Cube infrastructure so they are highly available and resilient for your workload and applications it's really about this but uh what do I mean by enabling High availability through multi sites So within this talk we're going to have two point of views from the app and from the infrastructure itself sorry uh shall it be uh on Prem thanks to there or in the cloud so yes what do I mean by buil sites anyway so usually working with customer on Prem again they Trend to have several facilities you know site a site B with dedicated power dedicated um rooms uh dedicated network uh Cooling and so on and so you know having multiple sites enables you to distribute your workload isolating them and making them more highly available usually two sides is not enough and you need a third one to avoid uh split brand scenarios uh Network partitioning and you can have a dedicated control plane somewhere else it can be also with a slightly higher latency it is CD is pretty tolerant according to the dock with high latency but over distribution um by by vendors like rat open ship distribution recommends you to have all these control planes spread within
