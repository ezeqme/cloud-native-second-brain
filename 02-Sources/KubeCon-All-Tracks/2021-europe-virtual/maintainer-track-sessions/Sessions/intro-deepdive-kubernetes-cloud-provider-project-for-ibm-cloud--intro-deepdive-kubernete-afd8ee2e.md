---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Sahdev Zala", "Richard Theis", "IBM"]
sched_url: https://kccnceu2021.sched.com/event/iE5x/intro-+-deepdive-kubernetes-cloud-provider-project-for-ibm-cloud-sahdev-zala-richard-theis-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Intro+%2B+DeepDive%3A+Kubernetes+Cloud+Provider+Project+for+IBM+Cloud+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Intro + DeepDive: Kubernetes Cloud Provider Project for IBM Cloud - Sahdev Zala & Richard Theis, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Sahdev Zala, Richard Theis, IBM
- Schedule: https://kccnceu2021.sched.com/event/iE5x/intro-+-deepdive-kubernetes-cloud-provider-project-for-ibm-cloud-sahdev-zala-richard-theis-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Intro+%2B+DeepDive%3A+Kubernetes+Cloud+Provider+Project+for+IBM+Cloud+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Intro + DeepDive: Kubernetes Cloud Provider Project for IBM Cloud.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE5x/intro-+-deepdive-kubernetes-cloud-provider-project-for-ibm-cloud-sahdev-zala-richard-theis-ibm
- YouTube search: https://www.youtube.com/results?search_query=Intro+%2B+DeepDive%3A+Kubernetes+Cloud+Provider+Project+for+IBM+Cloud+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HC6JSMVaRe8
- YouTube title: Intro + DeepDive: Kubernetes Cloud Provider Project for IBM Cloud - Sahdev Zala & Richard Theis, IBM
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/intro-deepdive-kubernetes-cloud-provider-project-for-ibm-cloud/HC6JSMVaRe8.txt
- Transcript chars: 23284
- Keywords: provider, openshift, cluster, interface, providers, provide, similar, release, running, security, richard, please, releases, provided, control, little, forward, controller

### Resumo baseado na transcript

all right hello everyone uh welcome to this talk kubernetes cloud provider project for ibm cloud my name is sadie zala i am a senior software engineer and open source developer at ibm i contribute to kubernetes uh i'm one of the maintenance for the fcd project and i am uh one of the co-lead for the provider ibm cloud project i have a pleasure of having richard thais with me today for recording of this talk so richard would you like to introduce yourself please yes thank you i'm the project downstream so proposals to go to three rather than four releases of kubernetes every year um believing that you know a lot of background investigation that's gone into it feedback surveys and such um so that i think have a good direction for um so we're going to look at pulling in and using the new interface a little bit more efficient for the new architecture the cloud provider so that's more of an implementation detail but nonetheless you can see the the moves forward in the community along with them uh the nice thing with the new design from the community is that we're able to now turn on and off interfaces that are interesting to us um for our i shouldn't say interfaces turn on off the um control loops that are of interest so if we're not using a control loop we can shut it off um now in the new version 120 from kubernetes so we'll go to the next slide and we'll look at some of the um...

### Excerpt da transcript

all right hello everyone uh welcome to this talk kubernetes cloud provider project for ibm cloud my name is sadie zala i am a senior software engineer and open source developer at ibm i contribute to kubernetes uh i'm one of the maintenance for the fcd project and i am uh one of the co-lead for the provider ibm cloud project i have a pleasure of having richard thais with me today for recording of this talk so richard would you like to introduce yourself please yes thank you i'm richard tys work for ibm as a software engineer on the ibm cloud kubernetes service and red hat open shift and ibm cloud managed services as the release lead for delivering openshift and kubernetes releases to our platform and with uh satay i'm co-chair for the cloud provider project for ibm cloud thank you well uh thank you richard um all right um hello again uh so for the agent uh you know we will provide uh an overview of uh sig cloud provider and uh this sub project provided ibm cloud uh you know this is a part of the maintenance track so we'll definitely give you some introduction here of the project uh we'll briefly cover activities and then we'll talk about cluster api provider for ibm cloud and the ibm cloud provider which richard will we give a deep dive all right so um you might already know about special interest group cloud provider it owns kubernetes cloud provider interface uh the code and related work uh you know which is responsible for running all the cloud providers specific control loops right so you know you know that when you run money like kubernetes on different uh cloud providers right they have their uh uh own requirements they have their own uh functionalities uh uh for for the communities right to run the keyboard is on on their site so for example load balancer right that's one of the examples there um so uh you can learn more about uh the the code there uh in the github repo for the cloud provider i have put a link here um the seek also ensures that the kubernetes ecosystem evolves in a way that is neutral to all the cloud providers right so there is no favor given to one cloud provider or other that kind of things uh it also ensures a consistent and high quality user experience across different cloud providers and the sig also owns uh the sub-projects from various cloud providers so for example uh the project we will be talking today uh the ibm cloud provider it's one of the sub project and you know some other examples are like provider aws required azu
