---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Xiangqian Yu", "Google"]
sched_url: https://kccncna2022.sched.com/event/182MZ/kubernetes-data-protection-wg-deep-dive-xiangqian-yu-google
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Deep+Dive+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes Data Protection WG Deep Dive - Xiangqian Yu, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Xiangqian Yu, Google
- Schedule: https://kccncna2022.sched.com/event/182MZ/kubernetes-data-protection-wg-deep-dive-xiangqian-yu-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Deep+Dive+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes Data Protection WG Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182MZ/kubernetes-data-protection-wg-deep-dive-xiangqian-yu-google
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Data+Protection+WG+Deep+Dive+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tgtROSKLKOU
- YouTube title: Kubernetes Data Protection WG Deep Dive - Xiangqian Yu, Google
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-data-protection-wg-deep-dive/tgtROSKLKOU.txt
- Transcript chars: 21244
- Keywords: volume, snapshot, bucket, application, backup, storage, actually, working, access, populator, source, support, however, restore, consistent, allows, called, provision

### Resumo baseado na transcript

let's get started uh right on time actually 30 seconds before welcome everybody my name is uh Sean Chen it's kind of hard just commission everybody commission I work for Google and standing next to me is she will go rich and working in the data protection group with xianchien we have a long agenda to go today so we'll try to go fast uh they generalize many to Deep dive into a couple of caps into this whole data protection working group or what are we doing uh what

### Excerpt da transcript

let's get started uh right on time actually 30 seconds before welcome everybody my name is uh Sean Chen it's kind of hard just commission everybody commission I work for Google and standing next to me is she will go rich and working in the data protection group with xianchien we have a long agenda to go today so we'll try to go fast uh they generalize many to Deep dive into a couple of caps into this whole data protection working group or what are we doing uh what kind of progresses were made so far and what problems are we trying to solve as Euro we'll start with motivation then move on to the organization that has been involved and actually pretty actively contributing into this working group and give this group here a little bit key updates what has happened in the past year or two and then we dupe into the Caps right those are the individual crops and lastly we'll close with how you folks can get involved who are you I believe everybody over here has been either a user of kubernetes or active contributor of the community so uh you probably are pretty aware of the fundamental constructs to support stateful workloads in the kubernetes environment namely persistent volume claims those are the user-facing API that gives you a volume as well as workload apis like State faucet deployment etc etc which in any of these open apis as of today allows you to attach a volume to your workload and when your workload you bring down your workout and bring it back again your volume processes so your data is not lost during the process uh another trend is that some of you I think I recognize it went to the data in kubernetes meeting on Monday right the trend is pretty obvious so more and more stateful workload is moving into kubernetes World initially the kubernetes actually has been built in a state where uh you can safely bring down and bring up your application at any given point of time and it scales for you but not a not a very fundamental problem to solve over here for state will work early is actually how do I make sure my data it's not in uh it's it's protected properly so day two operations for now in kubernetes is actually still having a couple of grabs over there there are tools there by saying that right like for example git Ops is very popular as of today to allow you save your configuration into a git repository while still allow you to do application low back and upgrade failures recovery etc etc however the main gaps has been noticed and found in the vari
