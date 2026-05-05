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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Ádám Rozmán", "Ericsson Software Technology", "Nicolas Belouin", "SUSE"]
sched_url: https://kccnceu2026.sched.com/event/2EF5z/beyond-the-cloud-managing-baremetal-the-kubernetes-way-using-metal3io-sylva-project-as-a-use-case-adam-rozman-ericsson-software-technology-nicolas-belouin-suse
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+the+Cloud%3A+Managing+Baremetal+the+Kubernetes+Way+Using+Metal3.io%3A+Sylva+Project+as+a+Use-case+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Beyond the Cloud: Managing Baremetal the Kubernetes Way Using Metal3.io: Sylva Project as a Use-case - Ádám Rozmán, Ericsson Software Technology; Nicolas Belouin, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ádám Rozmán, Ericsson Software Technology, Nicolas Belouin, SUSE
- Schedule: https://kccnceu2026.sched.com/event/2EF5z/beyond-the-cloud-managing-baremetal-the-kubernetes-way-using-metal3io-sylva-project-as-a-use-case-adam-rozman-ericsson-software-technology-nicolas-belouin-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+the+Cloud%3A+Managing+Baremetal+the+Kubernetes+Way+Using+Metal3.io%3A+Sylva+Project+as+a+Use-case+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Beyond the Cloud: Managing Baremetal the Kubernetes Way Using Metal3.io: Sylva Project as a Use-case.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5z/beyond-the-cloud-managing-baremetal-the-kubernetes-way-using-metal3io-sylva-project-as-a-use-case-adam-rozman-ericsson-software-technology-nicolas-belouin-suse
- YouTube search: https://www.youtube.com/results?search_query=Beyond+the+Cloud%3A+Managing+Baremetal+the+Kubernetes+Way+Using+Metal3.io%3A+Sylva+Project+as+a+Use-case+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pThPIOZ7Nb0
- YouTube title: Beyond the Cloud: Managing Baremetal the Kubernetes Way Using Metal... Ádám Rozmán & Nicolas Belouin
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/beyond-the-cloud-managing-baremetal-the-kubernetes-way-using-metal3-io/pThPIOZ7Nb0.txt
- Transcript chars: 26850
- Keywords: cluster, machine, firmware, provider, management, support, machines, address, basically, components, bootstrap, deploy, configuration, operator, provisioner, hardware, deployed, provisioning

### Resumo baseado na transcript

I'm from Ericson, more specifically Ericson software technology >> and I'm Nicolola Bulwa from Souza most specifically the engineering telco team. Today we will talk about uh beyond the cloud cloud managing bermatal the kubernetes way using the meta cube project and showing you silva project as a specific use case for meta cube integration. So on the top as you as as you can see we have cluster API standard Kubernetes component then we have an official provider for the cluster API in the form of the cluster API meta cube provider that's just an interface implementation we also In some cases in in some environments, you can reach your own uh your data center through some very complicated routing or you have very strict uh security rules or simply you don't have a DHCP server in that uh data center in that specific environment and you cannot bring your own. We have the same sort of leasing logic that you have in a DHCP server just written for uh Kubernetes and then that uh and we have pools that you can set up and then claims are generated against the pools and then the claims are served so or or fulfilled and then you have IP addresses attached to your nodes. uh that's the minimal custom resource that you have to deploy and and this and and uh one other components is the minimal deployment that you need to present a Kubernetes uh present a physical machine in a Kubernetes space.

### Excerpt da transcript

Welcome everyone. Thank you for joining us in this late stage of the event. I I see that uh many of you joined. I hope you will enjoy our presentation. My name is Adam Rosman. I'm from Ericson, more specifically Ericson software technology >> and I'm Nicolola Bulwa from Souza most specifically the engineering telco team. >> Yeah. Today we will talk about uh beyond the cloud cloud managing bermatal the kubernetes way using the meta cube project and showing you silva project as a specific use case for meta cube integration. So I'm a one of the maintainer of the meta cube project and I will first walk you through that what is the meta cube project. So the meta cube is a bare metal life cycle manager uh clustering tool and in general an end to end solution for many of the bare meta kubernetes problems that you might face uh in your career or in your project. You don't have to really memorize this uh picture. This is an reference architecture of the whole MACQ project. This only shows the active part. So the controllers that manage the life cycle from a very high multicluster level down to the nitty-gritty small uh course to the power cycling of a physical machine and so on.

So you can already see on this uh picture that there is a uh dashed line a dashed line in the middle and everything above that line is about multicluster management. If you don't want multicluster management or clustering of bare meta machines, you don't need that part. You can leave that off. But if you uh need that functionality, you have to take that part. And the part below the dash line is is uh purely about bare meta machine management, life cycle management, operating system installation, firmware updates, all these all these things that you have to do with a machine. So on the top you can see that we integrate with cluster API everywhere where you see the chevrons not the arrows those are interfaces and because there are interfaces in so many places this project is very modular and extendable and and you can configure it to your liking and we will see later an example from the sila project what parts they take and what parts they don't take. So on the top as you as as you can see we have cluster API standard Kubernetes component then we have an official provider for the cluster API in the form of the cluster API meta cube provider that's just an interface implementation we also have uh support for the cluster API IP address manager and we have our own IP address manager that also f
