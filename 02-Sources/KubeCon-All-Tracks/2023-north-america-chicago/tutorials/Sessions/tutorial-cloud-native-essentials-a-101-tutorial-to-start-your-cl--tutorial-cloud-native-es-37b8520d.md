---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Tutorials"
themes: ["Tutorials"]
speakers: ["Rey Lejano", "SUSE", "Eamon Bauman", "Red Hat"]
sched_url: https://kccncna2023.sched.com/event/1R2nY/tutorial-cloud-native-essentials-a-101-tutorial-to-start-your-cloud-native-journey-rey-lejano-suse-eamon-bauman-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Cloud+Native+Essentials%3A+A+101+Tutorial+to+Start+Your+Cloud+Native+Journey+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: Cloud Native Essentials: A 101 Tutorial to Start Your Cloud Native Journey - Rey Lejano, SUSE & Eamon Bauman, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[Tutorials]]
- País/cidade: United States / Chicago
- Speakers: Rey Lejano, SUSE, Eamon Bauman, Red Hat
- Schedule: https://kccncna2023.sched.com/event/1R2nY/tutorial-cloud-native-essentials-a-101-tutorial-to-start-your-cloud-native-journey-rey-lejano-suse-eamon-bauman-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Cloud+Native+Essentials%3A+A+101+Tutorial+to+Start+Your+Cloud+Native+Journey+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: Cloud Native Essentials: A 101 Tutorial to Start Your Cloud Native Journey.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2nY/tutorial-cloud-native-essentials-a-101-tutorial-to-start-your-cloud-native-journey-rey-lejano-suse-eamon-bauman-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Cloud+Native+Essentials%3A+A+101+Tutorial+to+Start+Your+Cloud+Native+Journey+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0RJBYVyHB3Q
- YouTube title: Tutorial: Cloud Native Essentials: A 101 Tutorial to Start Your Cloud N... Rey Lejano & Eamon Bauman
- Match score: 0.914
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-cloud-native-essentials-a-101-tutorial-to-start-your-cloud-na/0RJBYVyHB3Q.txt
- Transcript chars: 56716
- Keywords: container, install, docker, harbor, running, actually, control, cluster, command, create, namespace, prometheus, native, application, installed, simple, version, download

### Resumo baseado na transcript

all right so let's start welcome everyone Welcome to Cloud native Essentials a one1 tutorial to you start your Cloud native Journey uh first off a little bit about us I'll start by introducing myself my name is aan Balman I am a uh Solutions architect at Red Hat formerly with uh work with uh Ray Souza and uh Was An Architect at uh Rancher for a period of time so excited to be up here and uh help and deliver this talk and I'm Ray Lano I am a machine will be for container D kubernetes and uh all the other tooling all the other skep graduated projects like celium Prometheus and uh Opa okay so I'm going to click on start scenario we're going to wait a few minutes here um for instances text file we see 1283 is our latest version so let's take that 1283 and put that along with our architecture and the release version that we specified there into these environment variables we'll change directory into our download D and then we'll actually download a bunch of kubernetes tools Cub ADM cuet specifically we will run pseudo chod plus X and that's going to add the executable bit to those files and then we'll want to download the cuet systemd unit file so you can click to run that yaml with that enginex service created you can use Cube control get service and that shows that we have a node Port service running that means that on our kubernetes node here we are exposing port in this case...

### Excerpt da transcript

all right so let's start welcome everyone Welcome to Cloud native Essentials a one1 tutorial to you start your Cloud native Journey uh first off a little bit about us I'll start by introducing myself my name is aan Balman I am a uh Solutions architect at Red Hat formerly with uh work with uh Ray Souza and uh Was An Architect at uh Rancher for a period of time so excited to be up here and uh help and deliver this talk and I'm Ray Lano I am a cloud native solution uh architect at Susa uh by way of ranch Labs um I'm also a sen staff Ambassador as well I also uh was a kubernetes release lead and I'm a co-chair for Sig kubernetes Sig docs and a sub Project Lead for kubernetes Sig security so I do a few things in the kuber so um when I first started I had a hard time like where to start in my cloud native Journey I'm sure everyone here has seen the cloud native landscape and it is uh mindboggling and it is hard to determine where is a good place to start uh so even with specific sections like container runtime there's uh a lot of projects for container runtimes how do we know which one to choose same thing with uh with scheduling an orchestration uh do we use crossplane do we use kubernetes use Ked like there's so many options on what to choose where do we start uh like where do we go from which project to this project to another project so I took the the um inspiration from axant I had one in my garage growing up my dad was a Merchant Marine and axant uh takes two points of reference to find latitude so I we took um inspiration from my suant and we're we are taking two points of reference to determine our Cloud native Journey uh the first one being a gradual projects with the cncf and there's a filter uh in the clate landscape to find out uh to find graduated projects but it still hard there's still multiple choices so where do we go from there uh there's 24 cnep graduated projects the first one being kubernetes uh the ones highlighted here is what we are going to get handson with at the uh Hands-On portion of this tutorial uh so we we'll talk for about half an hour or so then we'll get hands on uh so where the first one was kubernetes and the last the latest one was cium so these are the projects that we'll go through and we will briefly talk about in the next few slides here so the second point of reference we need to determine our Cloud native journey is this Cloud native trail map uh so this was published in 2018 from the cncf this was uh published to help
