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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Michael McCune", "Red Hat", "Bridget Kromhout", "Microsoft", "Walter Fender", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1tcyK/sig-cloud-provider-deep-dive-testing-cloud-controller-managers-michael-mccune-red-hat-bridget-kromhout-microsoft-walter-fender-google
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Cloud+Provider+Deep+Dive%3A+Testing+Cloud+Controller+Managers+CNCF+KubeCon+2025
slides: []
status: parsed
---

# SIG Cloud Provider Deep Dive: Testing Cloud Controller Managers - Michael McCune, Red Hat; Bridget Kromhout, Microsoft; Walter Fender, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Michael McCune, Red Hat, Bridget Kromhout, Microsoft, Walter Fender, Google
- Schedule: https://kccnceu2025.sched.com/event/1tcyK/sig-cloud-provider-deep-dive-testing-cloud-controller-managers-michael-mccune-red-hat-bridget-kromhout-microsoft-walter-fender-google
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Cloud+Provider+Deep+Dive%3A+Testing+Cloud+Controller+Managers+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre SIG Cloud Provider Deep Dive: Testing Cloud Controller Managers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcyK/sig-cloud-provider-deep-dive-testing-cloud-controller-managers-michael-mccune-red-hat-bridget-kromhout-microsoft-walter-fender-google
- YouTube search: https://www.youtube.com/results?search_query=SIG+Cloud+Provider+Deep+Dive%3A+Testing+Cloud+Controller+Managers+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WeWQqQM6kjM
- YouTube title: SIG Cloud Provider Deep Dive: Testing Cloud Cont... Michael McCune, Bridget Kromhout & Walter Fender
- Match score: 0.803
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sig-cloud-provider-deep-dive-testing-cloud-controller-managers/WeWQqQM6kjM.txt
- Transcript chars: 35266
- Keywords: provider, testing, providers, network, walter, server, specific, controller, cluster, actually, getting, little, bridget, talking, interesting, future, question, interface

### Resumo baseado na transcript

So, welcome everyone to the SIG cloud provider deep dive where we're going to talk about testing uh cloud controller managers. Uh I'm a software engineer at Red Hat where I work on cloud providers and also cluster autoscaling and whatnot. general premise was let's stop let's just stop no more cloud provider code in KK the problem then is now you've got two classes of people operating you've got someone who's in tree and gets to do things and then you had a lot of going back to what you know Walter was talking about you know this cloud provider code has existed as part of Kubernetes since the 1.0 era and around the 1, you know, 13 time is when these decisions were made to start saying, okay, we need to start getting this stuff out of here. But something else we wanted to highlight as well is there used to be an SSH tunnel built into Kubernetes as well. Yeah, I mean so whether you're aware of it or not, it's not a required piece, but the API machinery code when the Kubernetes API server wants to talk to your cluster, it needs to be able to route traffic.

### Excerpt da transcript

So, welcome everyone to the SIG cloud provider deep dive where we're going to talk about testing uh cloud controller managers. And a little bit of an intro here to start with. Uh I'm Michael McCuin. Uh I'm a software engineer at Red Hat where I work on cloud providers and also cluster autoscaling and whatnot. And uh Bridget, yeah, I'm Bridget Crumbot and I am a product manager at Microsoft, a cloud pro SIG plug cloud provider co-chair. um focused on lots of upstream open-source CNCF stuff. Very exciting. Uh and yeah, Walter. Hey, I'm Walter. I'm an EM in denial. I I still pretend that I'm a SUI. I would like to keep pretending that I'm a Sui, but unfortunately sometimes I do actually have to act as an EM, but take it away, Walter. All right, so history time. Um, SIG cloud provider has started as a working group. Uh, Tim Hawin came and with a few other folks said, "Hey, our codebase at Kubernetes is getting very complicated." And this is before it got nearly as complicated as it is today. And a lot of that complication has to do with Google and well others, but largely at the time Google.

Uh, you can say that because you work at Google. I work at Google. I'm allowed to to take the blame, but the cloud providers had a lot of cloud provider specific code and you know anyone who's looked through what happens when you want an IP address for your node or you're trying to work out the node isn't responding anymore is the VM under it still in existence is quite familiar with how much actual cloud provider code is needed to make all of this work and every time we added a new cloud provider that complexity went up and so the general premise was let's stop let's just stop no more cloud provider code in KK the problem then is now you've got two classes of people operating you've got someone who's in tree and gets to do things and then you had a lot of secondary cloud providers who weren't in tree and it was fairly unfair to them and So, we started and we've been working very hard and as of I think it was about a year ago, we deleted over a million lines of code. All the cloud provider code is gone.

It's out of KK. I mean, red diffs are good diffs, right? Yeah. Yeah. And I mean, if you look at like this uh little timeline we've put together here, you can see the process of how long it took us to do this. going back to what you know Walter was talking about you know this cloud provider code has existed as part of Kubernetes since the 1.0 era and around the 1, you know
