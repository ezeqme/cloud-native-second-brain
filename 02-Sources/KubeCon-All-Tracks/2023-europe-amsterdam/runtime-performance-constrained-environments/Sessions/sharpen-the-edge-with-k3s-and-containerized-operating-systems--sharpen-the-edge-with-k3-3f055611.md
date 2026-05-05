---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Runtime Performance + Constrained Environments"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Rey Lejano", "SUSE"]
sched_url: https://kccnceu2023.sched.com/event/1HycI/sharpen-the-edge-with-k3s-and-containerized-operating-systems-rey-lejano-suse
youtube_search_url: https://www.youtube.com/results?search_query=Sharpen+the+Edge+with+K3s+and+Containerized+Operating+Systems+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Sharpen the Edge with K3s and Containerized Operating Systems - Rey Lejano, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Runtime Performance + Constrained Environments]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Rey Lejano, SUSE
- Schedule: https://kccnceu2023.sched.com/event/1HycI/sharpen-the-edge-with-k3s-and-containerized-operating-systems-rey-lejano-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Sharpen+the+Edge+with+K3s+and+Containerized+Operating+Systems+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Sharpen the Edge with K3s and Containerized Operating Systems.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HycI/sharpen-the-edge-with-k3s-and-containerized-operating-systems-rey-lejano-suse
- YouTube search: https://www.youtube.com/results?search_query=Sharpen+the+Edge+with+K3s+and+Containerized+Operating+Systems+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ipeUafMXurQ
- YouTube title: Sharpen the Edge with K3s and Containerized Operating Systems - Rey Lejano, SUSE
- Match score: 0.964
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/sharpen-the-edge-with-k3s-and-containerized-operating-systems/ipeUafMXurQ.txt
- Transcript chars: 25629
- Keywords: container, elemental, bootable, upgrade, docker, devices, controller, actually, toolkit, cluster, containerized, operating, device, network, clusters, kernel, setting, create

### Resumo baseado na transcript

hey folks welcome come on in happy Friday I got one more minutes okay two o'clock exactly uh welcome to sharpen the edge with k3s and containerized operating systems I am Ray lojano I work for Susa professionally but I'm also an upstream kubernetes contributor I am the Sig docs co-chair so I help maintain kubernetes dot IO the Upstream documentation I've been a member of seven release teams some of the highlights was I was the release lead for 1.23 I was the immersed advisor for 1.25 that that

### Excerpt da transcript

hey folks welcome come on in happy Friday I got one more minutes okay two o'clock exactly uh welcome to sharpen the edge with k3s and containerized operating systems I am Ray lojano I work for Susa professionally but I'm also an upstream kubernetes contributor I am the Sig docs co-chair so I help maintain kubernetes dot IO the Upstream documentation I've been a member of seven release teams some of the highlights was I was the release lead for 1.23 I was the immersed advisor for 1.25 that that removed pod security policies I'm also a sub-project lead for six security I helped run the external security audit that was published on Wednesday so please uh take a look at that and I have links here and these slides are updated and uploaded as well but today we're going to start off talking about what is the edge and uh the edge there's many definitions for it uh it could be a browser it could be a YouTube guitarist as well and if you ask multiple organizations you will get multiple answers a grocery store company might consider each location as an edge site but a bank may not consider each batch location in Edge site but only ATM machines not in a branch as as an edge site so um actually so we actually asked folks and organizations what uh what they uh Define as the edge so we got several answers uh from uh from that survey it could be any remote site or device that processes data and connected by a network some said it's any place that's not part of the organization's core Network or DC or cloud or it could be any Remote device that can sense infer and act by itself and there are many more different answers as well so but when I actually Googled what is Edge Computing there's also multiple answers but there is a trend I'm not going to go through the list but there's four common traits one it's a remote location away from the DC there's some sort of computes and processing involved and there's a network connection lastly I want to point out there the Linux Foundation has a state of the edge at lfedge.org please take a look at that it's a vendor neutral platform for research on edge computing so there's challenges to etch no matter what how or how people Define uh Edge locations one is a resource so there's resource constraints so you might have small devices this may not be totally true for uh every organization that like if an organ or like if an organization actually ships out um Hardware to host vcenter on uh that wouldn't be very resource constraint but it m
