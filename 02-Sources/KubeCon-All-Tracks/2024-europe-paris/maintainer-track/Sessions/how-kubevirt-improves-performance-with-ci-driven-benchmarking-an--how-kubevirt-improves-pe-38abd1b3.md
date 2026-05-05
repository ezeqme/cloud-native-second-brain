---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Ryan Hallisey", "Alay Patel", "Nvidia"]
sched_url: https://kccnceu2024.sched.com/event/1YhiB/how-kubevirt-improves-performance-with-ci-driven-benchmarking-and-you-can-too-ryan-hallisey-alay-patel-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=How+KubeVirt+Improves+Performance+with+CI-Driven+Benchmarking%2C+and+You+Can+Too+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How KubeVirt Improves Performance with CI-Driven Benchmarking, and You Can Too - Ryan Hallisey & Alay Patel, Nvidia

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Ryan Hallisey, Alay Patel, Nvidia
- Schedule: https://kccnceu2024.sched.com/event/1YhiB/how-kubevirt-improves-performance-with-ci-driven-benchmarking-and-you-can-too-ryan-hallisey-alay-patel-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=How+KubeVirt+Improves+Performance+with+CI-Driven+Benchmarking%2C+and+You+Can+Too+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How KubeVirt Improves Performance with CI-Driven Benchmarking, and You Can Too.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhiB/how-kubevirt-improves-performance-with-ci-driven-benchmarking-and-you-can-too-ryan-hallisey-alay-patel-nvidia
- YouTube search: https://www.youtube.com/results?search_query=How+KubeVirt+Improves+Performance+with+CI-Driven+Benchmarking%2C+and+You+Can+Too+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pCgLYXevN3Y
- YouTube title: How KubeVirt Improves Performance with CI-Driven Benchmarking, and You Can Too
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-kubevirt-improves-performance-with-ci-driven-benchmarking-and-you/pCgLYXevN3Y.txt
- Transcript chars: 19049
- Keywords: scalability, metrics, performance, number, cluster, server, running, actually, environment, virtual, cubert, control, monitor, benchmarks, benchmarking, important, machine, extensions

### Resumo baseado na transcript

test test okay all right we're going to get started D there's still room at the front if people do want to come I promise we don't bite okay uh it's early morning for me because I'm from the US so show of hands from everyone who in the audience loves virtual machines okay pretty good all right who in the audience show fans loves containers a lot more people okay I saw some people who didn't raise their hands though you must be here to see us talk about

### Excerpt da transcript

test test okay all right we're going to get started D there's still room at the front if people do want to come I promise we don't bite okay uh it's early morning for me because I'm from the US so show of hands from everyone who in the audience loves virtual machines okay pretty good all right who in the audience show fans loves containers a lot more people okay I saw some people who didn't raise their hands though you must be here to see us talk about scale and performance so I I appreciate that okay so I'm Ryan hesy I work at Nvidia as an engineer this is my colleague Al Patel also from Nvidia and we're here to talk about cicd driven benchmarking measuring scale and performance that that we do in cubert and we're excited to share with you today h talk to you about why this matters and share with you how you can do it too okay so first uh we'll begin I'll talk about uh at a high level cubert what it is uh and then I'll hand the mic over to LA and and he'll go through through talk about scalability how we measure scalability uh and then this idea of a control plane as a shared resource something really important to keep in the back of your mind as we're going through that control plane is a shared resource and then we'll talk a little bit about ke verts performance and scale stack and Benchmark so things in ways we measure and then we'll share with you how you can do this too as as someone who writes an an API someone who writes an operator how you can do the same thing that we're doing in cubert okay a virtual machine is a custom resource right so what does that mean it's it's an it's an extension of the kubernetes API so really when you're asking as the user for a virtual machine you're going to the kubernetes API server and what are you going to get you're actually going to get a container right so this interesting so for all the people who rais their hands for both that love virtual machines and containers just a shout out to you guys we also love virtual machines and containers in cubert because we rely on them very heavily so we get this container and we have the cubert control plane that does some work we have inside this container we've got a cumu process we've got Levert and then on the host we've got kvf we've got the hypervisor and so we do the cuber control plane does some work generates an XML and voila we're in France voila we have a we have a virtual machine and from there now you have a you think about it it's a virtual machine running insi
