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
themes: ["AI ML", "Community Governance"]
speakers: ["Rajith Attapattu", "Randoli"]
sched_url: https://kccnceu2026.sched.com/event/2EF6c/opencost-cost-and-resource-management-deep-dive-rajith-attapattu-randoli
youtube_search_url: https://www.youtube.com/results?search_query=OpenCost+-+Cost+and+Resource+Management+Deep+Dive+CNCF+KubeCon+2026
slides: []
status: parsed
---

# OpenCost - Cost and Resource Management Deep Dive - Rajith Attapattu, Randoli

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Rajith Attapattu, Randoli
- Schedule: https://kccnceu2026.sched.com/event/2EF6c/opencost-cost-and-resource-management-deep-dive-rajith-attapattu-randoli
- Busca YouTube: https://www.youtube.com/results?search_query=OpenCost+-+Cost+and+Resource+Management+Deep+Dive+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre OpenCost - Cost and Resource Management Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6c/opencost-cost-and-resource-management-deep-dive-rajith-attapattu-randoli
- YouTube search: https://www.youtube.com/results?search_query=OpenCost+-+Cost+and+Resource+Management+Deep+Dive+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QL3bpkNJRec
- YouTube title: OpenCost - Cost and Resource Management Deep Dive - Rajith Attapattu, Randoli
- Match score: 0.87
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/opencost-cost-and-resource-management-deep-dive/QL3bpkNJRec.txt
- Transcript chars: 23957
- Keywords: cost, pricing, little, question, architecture, source, vendors, cluster, resource, actually, support, running, container, allocation, opencast, prometheus, started, hopefully

### Resumo baseado na transcript

Like I said, I wasn't uh, you know, wasn't sure how many people are cared about costing Kubernetes. Um, I don't know if everybody's penny pinching or people have become wiser, but either way, I think it's a good thing to pay attention to. So it's an opportunity for you to um become a maintainer and hopefully that's one of the outcomes of this talk that I can at least uh influence a few of you to um drop by the open open source project the open cost project So we went past the sandbox uh stage and um keep an eye on the time and um we you know it provides the value of open cost is at a you know if I say it in a sentence it provides a cost model uh for kubernetes and it provides two things primarily one is the efficiency of your resource usage number two uh is the cost of u your resource usage and I'll get into the details in the in the next couple slides. People, you know, Kubernetes adoption is pretty mature these days and people thinking about day two ops and cost management uh is an essential part of it.

### Excerpt da transcript

Awesome. Okay. Um, happy to see all of you. Like I said, I wasn't uh, you know, wasn't sure how many people are cared about costing Kubernetes. Seems like a lot. Um, I don't know if everybody's penny pinching or people have become wiser, but either way, I think it's a good thing to pay attention to. Um, um, thanks a lot, uh, for giving your time today. Uh uh CubeCon's a very packed schedule. So I'm glad um all of you made the time here. Um and it's a pleasure and a privilege to come here and talk about uh Opencast. You guys can hear me at the back. All right. Awesome. Okay. Good. Um how many of you have heard about OpenCast? Yeah. Okay. Good. So we're probably doing a decent job about this. Yeah. Okay. Good. All right. So um let's get started. My name is Rajit Tatawatu. Um I'm the founder and CTO of Renoli. uh render is an observability platform um that also has uh cost visibility because we believe it's an essential part of uh observability and uh I'm also a maintainer of the open cost project and I'm here to talk to you guys about um you know opensource cost monitoring for Kubernetes.

Um how many of you showed up at the open cost booth today? O we need more. Okay, this time we got three days. Um, so just drop by and uh we can only offer you a sticker and um an a warm chat, but we'll take it. Yeah. Okay. Awesome. All right. So um what I want to do today is to introduce um open cost uh quickly talk a little bit about the architecture and also talk about what's new in open cost and then um talk a little bit of the road map and hopefully entice some of you to um contribute to open cost. Uh that's how my journey was as well. So you know when we were building observability platform um we needed to uh manage our own cost as well as um you know as a startup and we looked for solutions and we started using open cost and we realized it was so valuable we ended up using it in our product. That's how we got into it and then we started contributing uh and then we eventually you know sort of became part of the community and there are lots of um end users as well not just vendors end users as well who actually contribute maintain plugins etc.

So it's an opportunity for you to um become a maintainer and hopefully that's one of the outcomes of this talk that I can at least uh influence a few of you to um drop by the open open source project the open cost project by the Slack channel try it out and may perhaps submit a couple patches um you know um let's see how it goes
