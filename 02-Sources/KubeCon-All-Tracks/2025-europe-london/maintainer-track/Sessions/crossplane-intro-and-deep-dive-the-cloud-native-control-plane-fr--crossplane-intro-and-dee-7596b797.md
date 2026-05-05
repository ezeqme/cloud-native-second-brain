---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Jared Watts", "Nic Cope", "Upbound"]
sched_url: https://kccnceu2025.sched.com/event/1td15/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-nic-cope-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+The+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Crossplane Intro and Deep Dive - The Cloud Native Control Plane Framework - Jared Watts & Nic Cope, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Jared Watts, Nic Cope, Upbound
- Schedule: https://kccnceu2025.sched.com/event/1td15/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-nic-cope-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+The+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Crossplane Intro and Deep Dive - The Cloud Native Control Plane Framework.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td15/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framework-jared-watts-nic-cope-upbound
- YouTube search: https://www.youtube.com/results?search_query=Crossplane+Intro+and+Deep+Dive+-+The+Cloud+Native+Control+Plane+Framework+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6MrXcbcxnN4
- YouTube title: Crossplane Intro and Deep Dive - The Cloud Native Control Plane Framework - Jared Watts & Nic Cope
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/crossplane-intro-and-deep-dive-the-cloud-native-control-plane-framewor/6MrXcbcxnN4.txt
- Transcript chars: 34615
- Keywords: crossplane, resources, create, composition, basically, platform, function, namespace, cluster, define, crossplay, deployment, functions, language, manage, actually, resource, control

### Resumo baseado na transcript

Uh I think there's more room in the back there, but uh you know, grateful to see all your all's faces today. Um so we're obviously very excited to talk about something we're very passionate about. Crossplane basically extends Kubernetes and teaches it how to manage everything else. Crossplane aims to bring those into the Kubernetes control plane and allow you to provision and manage them from the control plane. So this S3 bucket here uh crossplane is representing it as an API object in the Kubernetes control plane. Just like any well- behaved um Kubernetes API object, they're going to have a status as well that's going to give you like the observed state of the real resource out there in the real world.

### Excerpt da transcript

All right, welcome everybody. Welcome, welcome. Still people filing in. Uh I think there's more room in the back there, but uh you know, grateful to see all your all's faces today. So, let's get this thing going. This is the crossplane talk. Uh my name is Jared. This is Nick. Uh we are part of the leadership of the Crossplane project. We've dedicated a good chunk of our careers now to crossplane. Um so we're obviously very excited to talk about something we're very passionate about. Um, as is usual for CubeCons, we have a very diverse range of uh, like experience levels with crossplane. So, some people are running it in production, some people have not even heard of crossplane before and they're curious about what it is. So, we do have to start this talk with 10 minutes of basic introductory stuff. the people the more crossplane pros might be a little bored with that but I guarantee you the second half uh is going to be quite interesting as Nick is talking about the the future of crossplane a v2 of crossplane very exciting stuff you haven't seen all right let's go so the basics what is crossplane so we like to think of uh crossplane as a cloudnative control plane you basically use it to provision and manage all of your resources uh you can take those resources you compose them into higher level abstractions and with those abstractions you offer those to your developers so that they can self-service and provision and get the resources they need.

Uh Kubernetes is a great control plane for containers. Crossplane basically extends Kubernetes and teaches it how to manage everything else. Um control planes are not a new concept, right? Cloud providers have been running control planes in their backends for years. Uh but now Crossplane gives you the framework and the tooling that you need to build your own control plane, your own platform. So the basic building blocks here, we call these managed resources in crossplane. Uh so think about all the different cloud providers out there, all the different SAS offerings, on premises software, all that stuff. There's thousands and thousands of different resources and services out there. Crossplane aims to bring those into the Kubernetes control plane and allow you to provision and manage them from the control plane. In practice, what that looks like here with a little practical example is imagine an S3 bucket. So this S3 bucket here uh crossplane is representing it as an API object in the Kubernetes control plane.

So ju
