---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Mariam Fahmy", "Nirmata", "Adam Crowder", "AWS"]
sched_url: https://kccnceu2026.sched.com/event/2CW5j/stop-flying-blind-real-time-enforceable-cluster-wide-quotas-with-kyverno-and-kro-mariam-fahmy-nirmata-adam-crowder-aws
youtube_search_url: https://www.youtube.com/results?search_query=Stop+Flying+Blind%3A+Real-Time%2C+Enforceable+Cluster-Wide+Quotas+with+Kyverno+and+KRO+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Stop Flying Blind: Real-Time, Enforceable Cluster-Wide Quotas with Kyverno and KRO - Mariam Fahmy, Nirmata & Adam Crowder, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mariam Fahmy, Nirmata, Adam Crowder, AWS
- Schedule: https://kccnceu2026.sched.com/event/2CW5j/stop-flying-blind-real-time-enforceable-cluster-wide-quotas-with-kyverno-and-kro-mariam-fahmy-nirmata-adam-crowder-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Stop+Flying+Blind%3A+Real-Time%2C+Enforceable+Cluster-Wide+Quotas+with+Kyverno+and+KRO+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Stop Flying Blind: Real-Time, Enforceable Cluster-Wide Quotas with Kyverno and KRO.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5j/stop-flying-blind-real-time-enforceable-cluster-wide-quotas-with-kyverno-and-kro-mariam-fahmy-nirmata-adam-crowder-aws
- YouTube search: https://www.youtube.com/results?search_query=Stop+Flying+Blind%3A+Real-Time%2C+Enforceable+Cluster-Wide+Quotas+with+Kyverno+and+KRO+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JtVMQmsI-4s
- YouTube title: Stop Flying Blind: Real-Time, Enforceable Cluster-Wide Quotas with Ky... Mariam Fahmy & Adam Crowder
- Match score: 0.878
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/stop-flying-blind-real-time-enforceable-cluster-wide-quotas-with-kyver/JtVMQmsI-4s.txt
- Transcript chars: 28247
- Keywords: resource, cluster, quotas, kyverno, essentially, policy, create, resources, created, validating, actually, kuberow, simply, request, budget, enforce, define, production

### Resumo baseado na transcript

We're going to talk about implementing dynamic cluster-wide resource quotas with Crow and Kyverno. Worked on a bunch of stuff there over the years, but nowadays I spend most of my time trying to make Kubernetes easier to use both within Amazon and externally as well. And then as pods come up in that namespace, Kubernetes can enforce that we're not essentially violating those those resource quotas. And so if we're taking a look at a solution here, how we can build something that essentially enforces a cluster-wide quota using these namespaced, we run into a few challenges here. And you know, we can write scripts and whatnot to query for these, but essentially there's no essentially native resource for this, right? We could just do this manually, we could write a bunch of scripts, we could maybe do this, you know, quote unquote properly and build like a Kubernetes controller for this that you know, is monitoring and managing these resources for us.

### Excerpt da transcript

Cool, thanks everyone for coming. We're going to talk about implementing dynamic cluster-wide resource quotas with Crow and Kyverno. But before we get into that, we'll start with some introductions. So hey, I'm Adam Crowder. I'm a software engineer at AWS. Specifically, I work on EKS, which is our Kubernetes offering. Worked on a bunch of stuff there over the years, but nowadays I spend most of my time trying to make Kubernetes easier to use both within Amazon and externally as well. Yeah, Miriam. Hi everyone. I'm Mariam Fahmy. I work as a software engineer at Cloudflare and I have been working in Kyverno for 2 years and a half and I'm one of the Kyverno maintainers. That's it. Awesome. Let's get into it. Yeah, just a second. The screens doesn't show our slides. Someone Oh, perfect. All right. So for this talk, we're going to walk through this theoretical scenario here where you're a platform engineer, you're running a Kubernetes cluster, right? For your team of developers. And specifically, you're running a multi-tenant Kubernetes cluster.

So we've got multiple teams operating within the cluster and each team as well has multiple different namespaces. So multi multi-tenant multi-namespace. And what we'd like to do is essentially enforce like a cluster-wide resource quota uh against essentially each team across namespaces. So if you're not familiar, Kubernetes has a native built-in resource called resource quotas. It's a namespace resource where you can essentially define like CPU and memory limits and stuff like that. And then as pods come up in that namespace, Kubernetes can enforce that we're not essentially violating those those resource quotas. So those are namespaced. And so if we're taking a look at a solution here, how we can build something that essentially enforces a cluster-wide quota using these namespaced, we run into a few challenges here. So let's say we're just orchestrating these individual namespace cluster resource quotas. So first of all, we don't really have a native way to aggregate across all the different namespaces.

We have to keep track of things like which namespaces are being used, where the resource quotas exist, which teams are associated with them, etc. And you know, we can write scripts and whatnot to query for these, but essentially there's no essentially native resource for this, right? Aside from that, we don't really have a good way to enforce budgets across namespaces. So if we want our developer teams to be able to t
