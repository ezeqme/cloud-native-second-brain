---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Stevie Caldwell", "Andy Suderman", "Fairwinds"]
sched_url: https://kccncna2025.sched.com/event/27FYn/patch-me-if-you-can-tackling-outdated-addons-before-they-become-a-risk-stevie-caldwell-andy-suderman-fairwinds
youtube_search_url: https://www.youtube.com/results?search_query=Patch+Me+If+You+Can%3A+Tackling+Outdated+Addons+Before+They+Become+a+Risk+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Patch Me If You Can: Tackling Outdated Addons Before They Become a Risk - Stevie Caldwell & Andy Suderman, Fairwinds

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Atlanta
- Speakers: Stevie Caldwell, Andy Suderman, Fairwinds
- Schedule: https://kccncna2025.sched.com/event/27FYn/patch-me-if-you-can-tackling-outdated-addons-before-they-become-a-risk-stevie-caldwell-andy-suderman-fairwinds
- Busca YouTube: https://www.youtube.com/results?search_query=Patch+Me+If+You+Can%3A+Tackling+Outdated+Addons+Before+They+Become+a+Risk+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Patch Me If You Can: Tackling Outdated Addons Before They Become a Risk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FYn/patch-me-if-you-can-tackling-outdated-addons-before-they-become-a-risk-stevie-caldwell-andy-suderman-fairwinds
- YouTube search: https://www.youtube.com/results?search_query=Patch+Me+If+You+Can%3A+Tackling+Outdated+Addons+Before+They+Become+a+Risk+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2SoLCWl800w
- YouTube title: Patch Me If You Can: Tackling Outdated Addons Before They Become... Stevie Caldwell & Andy Suderman
- Match score: 0.902
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/patch-me-if-you-can-tackling-outdated-addons-before-they-become-a-risk/2SoLCWl800w.txt
- Transcript chars: 28144
- Keywords: add-ons, upgrade, cluster, add-on, release, laughter, upgrading, little, version, fairwinds, clusters, security, testing, working, source, manager, manage, another

### Resumo baseado na transcript

Uh, welcome to our talk, patch me if you can, tackling outdated add-ons before they become a risk. Uh, my name is Stevie Caldwell and I am a tech lead for the SR team at Fairwinds. It's your big awesome application and you're very excited to share it with the world and you talk to someone and they said you should run this in a Kubernetes cluster. So you deploy a Kubernetes cluster and you deploy your baseline cluster, right? Now that you have traffic coming in, you're concerned about security, encryption, certificates. So add-ons, despite the name, which makes it sound like they're just kind of like nice to have are actually really integral to fulfilling the promise of Kubernetes and all the things that we expect out of it.

### Excerpt da transcript

Uh, good morning everyone. Uh, welcome to our talk, patch me if you can, tackling outdated add-ons before they become a risk. Uh, my name is Stevie Caldwell and I am a tech lead for the SR team at Fairwinds. I forgot to thank you. Uh, and uh, Fairwinds at Fairwinds we uh, build and manage Kubernetes clusters uh, add-ons and the underlying infrastructure. And uh joining me today is Andy. >> Hello everybody. I'm Andy. Uh thanks for joining us here early in the morning for some of us depending on what you did last night. [laughter] Um I am the CTO at Fairwinds. I'm a CNCF ambassador, former policy working group co-chair uh and author and maintainer of Pluto and Goldilocks, which are some open source tools that we have at Fairwinds. Stevie will not tell you because she's too humble, but she's also the author and maintainer of another open source project of Fairwinds called Go Nog Go, which we will mention a little bit later. Uh, and we're just super excited to have spent the last nine years contributing open source to the CNCF.

Uh, and to be here talking with you all about what we do to manage add-ons and some advice that we can give you all, uh, to keep your infrastructure up to date. >> Yeah. So, uh, I'm going to quickly go over the agenda. It's a very quick four-part agenda. Uh, we're going to talk about why add-ons matter. Um, we're going to talk about vulnerability trends that we're seeing in our space. We're going to talk about the operational struggle of managing add-ons. And then we're going to leave you with some best practices and tools and ideas for uh for tackling this uh those struggles yourselves. I >> think there was a joke you wanted to tell me. >> Yeah. So, before we get started though, I needed to ask you an important question. Huh? >> What do you call a computer floating in the ocean? >> Computer floating in the ocean. I don't Anybody know? >> Adele rolling in the deep. [laughter] >> Nice. That's good. That's good. >> Thank you. >> All right. So, let's start with talking about why add-ons matter. What are they? Why do we have them?

I'm gonna take you on a journey and you all are going to be the uh you know the the the the uh person the core character in this journey. You wrote an application. It's your big awesome application and you're very excited to share it with the world and you talk to someone and they said you should run this in a Kubernetes cluster. So you deploy a Kubernetes cluster and you deploy your baseline cluster, right? So
