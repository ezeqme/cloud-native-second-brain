---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Shaikh Israil", "John Moore", "Oracle America Inc"]
sched_url: https://kccncna2023.sched.com/event/1R2oe/burden-to-bliss-eliminate-patching-and-upgrading-toil-with-cluster-autoscaler-at-scale-shaikh-israil-john-moore-oracle-america-inc
youtube_search_url: https://www.youtube.com/results?search_query=Burden+to+Bliss%3A+Eliminate+Patching+and+Upgrading+Toil+with+Cluster+Autoscaler+at+Scale+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Burden to Bliss: Eliminate Patching and Upgrading Toil with Cluster Autoscaler at Scale - Shaikh Israil & John Moore, Oracle America Inc

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Shaikh Israil, John Moore, Oracle America Inc
- Schedule: https://kccncna2023.sched.com/event/1R2oe/burden-to-bliss-eliminate-patching-and-upgrading-toil-with-cluster-autoscaler-at-scale-shaikh-israil-john-moore-oracle-america-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Burden+to+Bliss%3A+Eliminate+Patching+and+Upgrading+Toil+with+Cluster+Autoscaler+at+Scale+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Burden to Bliss: Eliminate Patching and Upgrading Toil with Cluster Autoscaler at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2oe/burden-to-bliss-eliminate-patching-and-upgrading-toil-with-cluster-autoscaler-at-scale-shaikh-israil-john-moore-oracle-america-inc
- YouTube search: https://www.youtube.com/results?search_query=Burden+to+Bliss%3A+Eliminate+Patching+and+Upgrading+Toil+with+Cluster+Autoscaler+at+Scale+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O2baeDndNqU
- YouTube title: Burden to Bliss: Eliminate Patching and Upgrading Toil with Cluster Au... Shaikh Israil & John Moore
- Match score: 0.902
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/burden-to-bliss-eliminate-patching-and-upgrading-toil-with-cluster-aut/O2baeDndNqU.txt
- Transcript chars: 36982
- Keywords: infrastructure, cluster, little, actually, rotation, autoscaler, wanted, version, basically, simple, deployment, regions, scaler, question, patching, rotator, existing, another

### Resumo baseado na transcript

hello everyone um Welcome to our talk we are here to share our experiences on how we reduced the devops toil on eliminating the patching and up uh upgrading toil with cluster autoscaler so I'm Shake Israel and I go by Israel um I've been with Oracle for the last 3 years and I'm I'm just starting out in the kubernetes world and I've I'm I'm actually really loving it so I'm a kubernetes Enthusiast and I actually I'm very passionate about solving distributed system problems I am really enjoying

### Excerpt da transcript

hello everyone um Welcome to our talk we are here to share our experiences on how we reduced the devops toil on eliminating the patching and up uh upgrading toil with cluster autoscaler so I'm Shake Israel and I go by Israel um I've been with Oracle for the last 3 years and I'm I'm just starting out in the kubernetes world and I've I'm I'm actually really loving it so I'm a kubernetes Enthusiast and I actually I'm very passionate about solving distributed system problems I am really enjoying this this is my first conference by the way and I'm very excited to be here to be on so many talks and meet so many people here so thank you cubec con for arranging this uh Hey folks uh my name is John Moore most people call me J Mo uh I am an SRE by trade uh probably got somewhere close to 20 years now in the industry um started off in networking and stumbl my way through programming eventually got to um basically data stores I don't know what it is about them but I fell in love with them uh loved mongodb I don't know what it was about it but document databases really turned the turned the page for me um before I knew it I started playing around with kubernetes and honestly I'm never going to look back so first of all a little bit about us and kind of where why we're here um Israel and I we work in oci that's the Oracle Cloud infrastructure uh we operate the service known as OSS which is the Oracle streaming service so much like Kinesis and AWS um we offer a fully scalable streaming environment that customers can use for all of their data in Motion in real-time use cases behind the scenes it's incred incredibly run on top of kubernetes with a lot of staple sets we deal with customers data and we take that very very serious seriously so whenever we're talking about scale we're usually talking about maintaining uptime and availability of these backend systems but we're also talking about the sheer number of regions that we offer our service in so little terminology um cluster autoscaler is typically called the ca um I call it the cast because sometimes when I hear people say I'm going to go rotate a CA I just have like a minor cardiac infarction I'm sure some of you folks know what I'm talk this guy's shaking his head he knows what's going on yeah scares you right uh so I just call the cast it makes explaining stuff to people so much easier U so if I say it and I sound wrong um I'm just weird uh ok if I drop that that's our version of our our kubernetes environment um s
