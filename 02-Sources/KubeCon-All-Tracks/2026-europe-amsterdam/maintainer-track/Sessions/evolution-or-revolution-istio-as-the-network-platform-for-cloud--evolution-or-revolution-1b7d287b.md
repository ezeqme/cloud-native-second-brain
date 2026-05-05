---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Platform Engineering", "Networking", "Community Governance"]
speakers: ["Mitch Connors", "Microsoft", "Daniel Grimm", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2EF4C/evolution-or-revolution-istio-as-the-network-platform-for-cloud-native-mitch-connors-microsoft-daniel-grimm-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Evolution+or+Revolution%3A+Istio+as+the+Network+Platform+for+Cloud+Native+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Evolution or Revolution: Istio as the Network Platform for Cloud Native - Mitch Connors, Microsoft & Daniel Grimm, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Networking]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mitch Connors, Microsoft, Daniel Grimm, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2EF4C/evolution-or-revolution-istio-as-the-network-platform-for-cloud-native-mitch-connors-microsoft-daniel-grimm-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Evolution+or+Revolution%3A+Istio+as+the+Network+Platform+for+Cloud+Native+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Evolution or Revolution: Istio as the Network Platform for Cloud Native.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4C/evolution-or-revolution-istio-as-the-network-platform-for-cloud-native-mitch-connors-microsoft-daniel-grimm-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Evolution+or+Revolution%3A+Istio+as+the+Network+Platform+for+Cloud+Native+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4K6s5y8HoBc
- YouTube title: Evolution or Revolution: Istio as the Network Platform for Cloud Nat... Mitch Connors & Daniel Grimm
- Match score: 0.921
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/evolution-or-revolution-istio-as-the-network-platform-for-cloud-native/4K6s5y8HoBc.txt
- Transcript chars: 29697
- Keywords: actually, mesh, gateway, multicluster, cluster, tunnel, control, network, traffic, envoy, running, features, zunnel, little, routing, started, working, always

### Resumo baseado na transcript

Uh we're going to be discussing whether the change in changes that are happening in the STTO project are evolution or revolution. Before we get started, you never know how to write one of these maintainer track talks. Uh you've got resources like mixer mixer and o that don't really exist in architectures today. all the way back in 2017, one of the uh design docs where we talked about project direction. You had to restart every pod to have it upgrade its sidecar and it wasn't really visible in the Kubernetes API at a high level which ones had the new sidecar which ones had the old sidecar. So, we introduced the Z tunnel, a layer 4 proxy that runs per node uh outside of the cluster and handles just MTLS and security because that's the only thing that every pod needs uh is MTLS and layer 4 security.

### Excerpt da transcript

Uh thank you for coming to the STO maintainer track talk. Uh we're going to be discussing whether the change in changes that are happening in the STTO project are evolution or revolution. Is this just a continuing iteration or is it something entirely new? Before we get started, you never know how to write one of these maintainer track talks. So I want to see if we can divide the audience into two camps. Uh one camp is I'm not really sure what ISTTEO is. I've heard about service mesh a little bit and I want to learn more. And the other camp is I'm I'm pretty familiar with ISTTO. I just want to hear what the latest and greatest is. So, who wants to learn what ISTTO is? How many of those have we got? Oh my gosh. >> Oh wow, that's a lot of you. >> I kind of thought it might be like that. And how about the ladder camp? Who just wants to hear what the latest and greatest in the project is? >> Okay, so like 2/3 on the first and one third on the second. >> I'd say almost 50/50, honestly. But yeah. >> Yeah. Okay. Well, we'll make sure to try to dial the content on that.

Uh my name is Mitch Connors. Uh I'm a principal software engineer at Microsoft. Uh I've also just joined the product managing management team for AKS networking. I'm a maintainer of the ISTO project since 2018 or 19. Uh and I'll have Daniel introduce himself. >> Yeah, my name is Daniel. I'm a software engineer at Redhead and I've been working on ISTO since I joined Red Hat actually in 2019. Yeah. So it's coming up to be seven years. >> Yeah, it's always cool to give a talk with somebody who came up together in the project at about the same time. So, uh, our agenda today, we're going to take some time looking back on where ISTSTEO has been, what the original design was for the project back in 2017. Uh, we're going to look at how health is doing. Are we still seeing active contributions and maintenance? And then, uh, we're going to talk through some of what's new in ISTSTEO and given the feedback we received along the way, we're going to make an effort to make sure that we're kind of giving this at as much of a 101 level as we can.

Let's launch into this. Uh, ISTTO0.1 launched in 2017. Uh, and we still maintain the website today. I was kind of impressed that we do that. You can go back to archive.istto.io and see all the old stuff. >> Maintain is a stretch, but it's there. >> Oh, yeah. I mean, it's it's horrible looking, but it it exists. Uh, and this was sort of the architectural diagram on how we
