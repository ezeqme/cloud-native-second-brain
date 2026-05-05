---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Jussi Nummelin", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyT/project-lightning-talk-k0s-cncf-sandbox-distro-updates-jussi-nummelin-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+k0s+-+CNCF+Sandbox+Distro+Updates+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: k0s - CNCF Sandbox Distro Updates - Jussi Nummelin, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jussi Nummelin, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyT/project-lightning-talk-k0s-cncf-sandbox-distro-updates-jussi-nummelin-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+k0s+-+CNCF+Sandbox+Distro+Updates+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: k0s - CNCF Sandbox Distro Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyT/project-lightning-talk-k0s-cncf-sandbox-distro-updates-jussi-nummelin-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+k0s+-+CNCF+Sandbox+Distro+Updates+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8iC49a-h3LU
- YouTube title: Project Lightning Talk: k0s - CNCF Sandbox Distro Updates - Jussi Nummelin, Maintainer
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-k0s-cncf-sandbox-distro-updates/8iC49a-h3LU.txt
- Transcript chars: 3640
- Keywords: control, actually, worker, cluster, working, deploy, whether, containerd, windows, sandbox, everything, single, binary, course, controller, processes, clusters, kosmodrome

### Resumo baseado na transcript

Um so, with K0s we actually package everything you need to run Kubernetes in a one single binary. So, you can actually deploy the same same single binary virtually anywhere.

### Excerpt da transcript

Hey, I'm Jussi. I'm one of the K0s core maintainers working at Mirantis. So, K0s, it's there's a lot of similarities with K3s. Yes. Both are slim and versatile and all that. Um so, with K0s we actually package everything you need to run Kubernetes in a one single binary. It's statically compiled, comes with all the dependencies embedded. So, you can actually deploy the same same single binary virtually anywhere. Whether it's Alpine, whether it's Red Hat, whether it's Ubuntu. It just works. Of course, we include all the batteries, but you can swap them out. Say you want to run CRI-O instead of Containerd, you just install CRI-O and point K0s to use that and it'll be fine. The kind of architectural difference compared to say your vanilla Kubernetes kubeadm setup is that that we do a a super clear separation of control plane and a worker plane. What I mean by that is that by default when you launch a K0s controller node, it's not going to run kubelet. It's not going to run even Containerd. So, it just runs the controller processes like API servers, get schedulers and and so on, right?

What that gives you is a lot of flexibility how you deploy your clusters. I could now as a stupid example, deploy my control plane node as an EC2 instance in Amazon, expose it to public internet, like that's a good idea, right? And then I could run my worker node in my basement on set of Raspberry Pis and as long as the worker node can call home, everything works. We use this connectivity to do kind of reverse tunneling, so the communications is kind of turned actually upside down. Which comes to a kind of a sibling project that we have called Kosmodrome. Because now if you think about it, what's control plane? Couple of Go lang processes and a database of sorts. Why do we make management of that complex? Because it's not, right? So, we thought that why can't we run that stuff in cluster as a pods and services and whatnot? So, Kosmodrome is set of controllers that actually gets you a declarative way to manage your control planes. And not only that, it also acts as a set of cluster API providers. So, now you get full stack management in a declarative way.

You define your control planes as custom resources, you define your whole infrastructure as cluster resources and boom, you can manage hundreds, thousands of clusters super easily without having the need to spin up VMs for the control plane. Um couple of highlights for the from the last release. Yes, we are also working with W
