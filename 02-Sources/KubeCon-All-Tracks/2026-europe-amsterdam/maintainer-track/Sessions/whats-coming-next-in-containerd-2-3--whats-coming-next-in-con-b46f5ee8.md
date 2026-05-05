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
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Mike Brown", "IBM", "Krisztian Litkey", "Intel"]
sched_url: https://kccnceu2026.sched.com/event/2EF4U/whats-coming-next-in-containerd-23-mike-brown-ibm-krisztian-litkey-intel
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+Coming+Next+in+Containerd+2.3%3F+CNCF+KubeCon+2026
slides: []
status: parsed
---

# What's Coming Next in Containerd 2.3? - Mike Brown, IBM & Krisztian Litkey, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mike Brown, IBM, Krisztian Litkey, Intel
- Schedule: https://kccnceu2026.sched.com/event/2EF4U/whats-coming-next-in-containerd-23-mike-brown-ibm-krisztian-litkey-intel
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+Coming+Next+in+Containerd+2.3%3F+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre What's Coming Next in Containerd 2.3?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4U/whats-coming-next-in-containerd-23-mike-brown-ibm-krisztian-litkey-intel
- YouTube search: https://www.youtube.com/results?search_query=What%27s+Coming+Next+in+Containerd+2.3%3F+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_mg1LtSNVCg
- YouTube title: What's Coming Next in Containerd 2.3? - Mike Brown, IBM & Krisztian Litkey, Intel
- Match score: 0.728
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/whats-coming-next-in-containerd-2-3/_mg1LtSNVCg.txt
- Transcript chars: 26019
- Keywords: container, plugins, basically, changes, containerd, plug-in, support, runtime, containers, attributes, creation, working, release, actually, cluster, validator, plugin, sandbox

### Resumo baseado na transcript

I I did the cry containerd plugin with lantaloo also known as random way back when and been working on it ever since. We work with the Kubernetes team, work with Docker, we work with Rancher, you know, pretty much anybody who wants to have a client or is trying to extend the, you know, containerd end up working with them or somebody else, one of the other maintainers. Um but it's key to recognize here that we're you know we're gonna also support performance management of the pods and containers. Kubernetes pod sand we did other sandbox types and new CRD controllers. Our release cadence for containerd is going to become like not unlike the kubernetes release cadence. It also uh whether it's LTS or not defines whether or not we can bring back uh new features in into a a particular release that you might need and and Kubernetes, right?

### Excerpt da transcript

Hello everybody. Thank you for joining us. I'm one of the containerd core maintainers. Been working on it since the beginning. I I did the cry containerd plugin with lantaloo also known as random way back when and been working on it ever since. I'm a sign member. We work with the Kubernetes team, work with Docker, we work with Rancher, you know, pretty much anybody who wants to have a client or is trying to extend the, you know, containerd end up working with them or somebody else, one of the other maintainers. I don't think I see Phil or Airauda. They should be here today. Um, hopefully at at the end of the session, we'll have questions and maybe we can answer most of them. Okay. And we have other contributors in the audience. Raise your hand if you've contributed to containerd. Okay. All right. I'll be looking in this d. There's a curse. Thank you, sir. Found them. Uh, so we're a CNCF graduated project since 2019. As I say, the we have a lot of public repos. Everything from snapshoters uh to nerdctl and nerd bucks.

quite quite a few very interesting projects. We'll be talking about NRI later on which is a a plug-in model that works with both containerd and cryo. All right. Uh everything in containerd we we try to be uh not opinionated and to allow other tools other clients as well as run times to be able to work with us and extend uh containerd. So as such it's become very popular and is probably in most of the clouds today. Okay. We we support uh remote snapshoters. Some of the new stuff that's you know has been added over the last few years. Um and we've got more new snapshers. Earos for example. There's Wom runtimes uh has been added as as far as having a new type of runtime. CDI uh we we had a container orchestrated device workg groupoup that came up with the CDI CDI plan and now CDI is supported by DRA controllers. So it's been a few years but it's now enabled by default inside of the 1.7 and above uh containerds. Okay. NRI nextG plugins. That's what uh Christian's going to be covering. Um but it's key to recognize here that we're you know we're gonna also support performance management of the pods and containers.

Okay. Uh anything VMs and anything that gets executed will have some new new ways to configure them using the NRI. Uh Kubernetes pod sandboxes. Uh the original sandbox that we supported in of course in containerd was the pod sandbox through the cry api and there's now now different ways to support pod sandboxes. For example, kata contain
