---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Jared Watts", "Nic Cope", "Upbound"]
sched_url: https://kccncna2023.sched.com/event/1R2ne/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-nic-cope-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+the+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Crossplane Intro and Deep Dive - the Cloud Native Control Plane Framework - Jared Watts & Nic Cope, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Jared Watts, Nic Cope, Upbound
- Schedule: https://kccncna2023.sched.com/event/1R2ne/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-nic-cope-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+the+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Crossplane Intro and Deep Dive - the Cloud Native Control Plane Framework.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2ne/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-nic-cope-upbound
- YouTube search: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+the+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=I5Rd0X7AROw
- YouTube title: Crossplane Intro and Deep Dive - the Cloud Native Control Plane Framework - Jared Watts & Nic Cope
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framewor/I5Rd0X7AROw.txt
- Transcript chars: 39237
- Keywords: crossplane, resources, function, resource, functions, bucket, everything, composition, abstraction, configuration, developer, infrastructure, platform, cluster, actually, release, control, providers

### Resumo baseado na transcript

We are both creators, maintainers, steering committee folks for Crossplane. So, this is a combined session as we do every year with both an intro and a deep dive part, right? Just like any good Kubernetes object, all the Crossplane resources also follow a consistent resource model. So, if we work our way from the left side of the diagram over to the right, we'll see that we start with a buckets custom resource, and then, you know, you as a user can use kubectl, GitOps, whatever you want to apply that to your Kubernetes cluster. And then underneath that, there is all sorts of Kubernetes common functionality. And then all the Kubernetes API machinery, the resource model, the runtime, all that stuff is very heavily used as well.

### Excerpt da transcript

All right, let's go ahead and get this session started here. I think it's just about right on time. Folks are coming in here, but that's all good. There's plenty of room more on the right side here, too. Come on in. All right. So, this is the Crossplane introduction and deep dive session. My name is Jared Watts. Right there is co-speaker Nick Cope coming on right away here. We are both creators, maintainers, steering committee folks for Crossplane. So, it is definitely a project that is near and dear to our hearts. All right. So, this is a combined session as we do every year with both an intro and a deep dive part, right? So, we're going to get into the introduction stuff that some of you all may have seen. Maybe you're a refresher for some of you, but we got to start with what Crossplane actually is. So, the best way to think about Crossplane is that it is a framework for building your own opinionated cloud-native control plane. You don't You shouldn't have to write any code to do that. We'll talk a little bit later on in the session about ways that you can now actually write code, but you should be able to do it, you know, create your own opinionated control plane in a declarative fashion.

So, the cloud providers, they've been running control planes for years, right? They manage their infrastructure with control planes, and so Crossplane gives you a way to be able to to essentially build your own in your own opinionated way to run your infrastructure. It's important to think about Crossplane as, you know, a project in the middle there with a top layer and a bottom layer. So, on the bottom, you've got an extensibility story for providers that can teach Crossplane pretty much to manage any infrastructure in any environment as long as it has an API. And then on the top layer, you can essentially compose resources together and then offer them as a new platform API and as an as an abstraction to your developers. So, it's extensible on both the front end and the back end. Might not make sense yet, but we will see it as it keeps going on here. Just a little bit of background history of the project. We are coming up on 5 years in the Crossplane project. We took it public in December of 2018.

So, next month it'll be 5 years. Pretty excited about that. We donated it to the CNCF in 2020. Then we've been continuing to mature along there. We're in the incubating stage now, and we're hoping next year to do the to move to a fully graduated stage. And we'll need your
