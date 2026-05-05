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
themes: ["AI ML", "Runtime Containers", "Kubernetes Core", "Community Governance"]
speakers: ["Harshal Patil", "Red Hat"]
sched_url: https://kccnceu2025.sched.com/event/1tcxn/enhancing-cri-o-with-cdi-streamlining-device-integration-in-kubernetes-harshal-patil-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Enhancing+CRI-O+With+CDI%3A+Streamlining+Device+Integration+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Enhancing CRI-O With CDI: Streamlining Device Integration in Kubernetes - Harshal Patil, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Harshal Patil, Red Hat
- Schedule: https://kccnceu2025.sched.com/event/1tcxn/enhancing-cri-o-with-cdi-streamlining-device-integration-in-kubernetes-harshal-patil-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Enhancing+CRI-O+With+CDI%3A+Streamlining+Device+Integration+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Enhancing CRI-O With CDI: Streamlining Device Integration in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcxn/enhancing-cri-o-with-cdi-streamlining-device-integration-in-kubernetes-harshal-patil-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Enhancing+CRI-O+With+CDI%3A+Streamlining+Device+Integration+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7-JtDLNT0c8
- YouTube title: Enhancing CRI-O With CDI: Streamlining Device Integration in Kubernetes - Harshal Patil, Red Hat
- Match score: 0.944
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/enhancing-cri-o-with-cdi-streamlining-device-integration-in-kubernetes/7-JtDLNT0c8.txt
- Transcript chars: 20792
- Keywords: device, container, gpu, essentially, devices, driver, nvidia, plug-in, resource, runtime, inside, created, create, qualified, resources, without, configuration, hardware

### Resumo baseado na transcript

Uh I am Harsh Patil and I will be talking about uh enhancing the device support in Kubernetes using something called CDI uh and how it interacts with cryo uh CR runtime. Uh so roughly the agenda we would go over what is cryo overview of cryo overview of CDI fundamentals like what's a CDI how it is defined uh how CDI is integrated in cryo and some practical applications and use cases of uh integration of There's nothing else cryo for there is nothing else we know no other way to use cryo other than using it via kubernetes like uh so that is where that is where we believe that minimizing this attack surface helps makes cryo a more secure CR runtime uh we're also very quick to adapt to new security for example uh we have something called safecom artifact support so essentially you can have your safe car configuration nicely kept somewhere in registry and we'll pull it and apply the seccom profile. designed and we will dive deeper into that but before that who should generally know about CDI like so for example For example, if you are a manufacturer of an accelerator like say GPU or if you have custom hardware like FPGAs or for that matter any device any device that you want to be used inside a container in Kubernetes uh and which requires complex setup.

### Excerpt da transcript

Good afternoon everyone. Uh thanks all for coming. Uh I am Harsh Patil and I will be talking about uh enhancing the device support in Kubernetes using something called CDI uh and how it interacts with cryo uh CR runtime. Uh so roughly the agenda we would go over what is cryo overview of cryo overview of CDI fundamentals like what's a CDI how it is defined uh how CDI is integrated in cryo and some practical applications and use cases of uh integration of CDI with the cryo we can we can have some time for Q&A also at the end uh so why cryo it's a cryo if you see it's it's CRI runtime. But what sets Cryo apart is that it is completely oriented towards uh Kubernetes. In a sense, it does everything in its existence. It does it for being with Kubernetes. So including the release cycles, the feature development, um there's nothing else for cryo to do apart from just being inside a Kubernetes cluster. So that's kind of keeps it uh helps us essentially uh do optimizations. Uh for example when you do when a generic plague tries to list parts in cubate cryohazard optimization to uh return faster without hitting the uh without traversing the croup fs uh using cache.

Uh we also have experimental features in developing cryo. We use annotations for that and cryo is also designed from the security point of view where you know because it only targets Kubernetes the attack surface is very limited. There's nothing else cryo for there is nothing else we know no other way to use cryo other than using it via kubernetes like uh so that is where that is where we believe that minimizing this attack surface helps makes cryo a more secure CR runtime uh we're also very quick to adapt to new security for example uh we have something called safecom artifact support so essentially you can have your safe car configuration nicely kept somewhere in registry and we'll pull it and apply the seccom profile. Uh so uh moving on this is generally how a CR runtime will look like. The gRPC is a CRI interface and where you have image service, you have runtime service and different components that cryo interacts with in order to u run the containers. Uh going forward and these are the these are the some of the some of the or adapters which which essentially help us stay motivated to make cryo better and better with every release.

U now going to the CDI aspect of it. So what is a CDI? uh it's essentially the if you expand it it's it translates to container device interface and uh it's a specificati
