---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["AI ML", "Security", "Networking"]
speakers: ["James Cleverley-Prance", "ControlPlane"]
sched_url: https://kccnceu2022.sched.com/event/ytu7/three-surprising-k8s-networking-features-and-how-to-defend-against-them-james-cleverley-prance-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Three+Surprising+K8s+Networking+%E2%80%9CFeatures%E2%80%9D+and+How+to+Defend+Against+Them+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Three Surprising K8s Networking “Features” and How to Defend Against Them - James Cleverley-Prance, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]], [[Networking]]
- País/cidade: Spain / Valencia
- Speakers: James Cleverley-Prance, ControlPlane
- Schedule: https://kccnceu2022.sched.com/event/ytu7/three-surprising-k8s-networking-features-and-how-to-defend-against-them-james-cleverley-prance-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Three+Surprising+K8s+Networking+%E2%80%9CFeatures%E2%80%9D+and+How+to+Defend+Against+Them+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Three Surprising K8s Networking “Features” and How to Defend Against Them.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytu7/three-surprising-k8s-networking-features-and-how-to-defend-against-them-james-cleverley-prance-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Three+Surprising+K8s+Networking+%E2%80%9CFeatures%E2%80%9D+and+How+to+Defend+Against+Them+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7iwnwbbmxqQ
- YouTube title: Three Surprising K8s Networking “Features” and How to Defend Against Them - James Cleverley-Prance
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/three-surprising-k8s-networking-features-and-how-to-defend-against-the/7iwnwbbmxqQ.txt
- Transcript chars: 19949
- Keywords: address, packet, cluster, network, source, little, bastion, destination, running, prevent, information, script, achieve, packets, attacker, concept, attack, expect

### Resumo baseado na transcript

good afternoon everyone and welcome to three surprising kubernetes networking features and how to defend against them so just a little bit of a background about me uh i used to be a penetration tester and these days i work at control plane uh predominantly being a security consultant but i also help out with training and workshops and contribute to our ctf events such as the one we ran at cloud native security days so what are we going to talk about today we're going to run through the api server listens so in this instance we can see that it contains the ip address of the api server kubernetes service which is an information leak which could help us determine the kubernetes service network range this will be important later the api server that's slightly wrapped hopefully you should be able to see that we have the core dns service the default kubernetes service and this other dashboard in the default namespace so we should be able to just connect to that dashboard to see what it presents let's try it and as we can see we can connect direct to that service ip from our bastion without any authentication we're going to take this a step further and query core dns for all the service endpoints so these are all the pod

### Excerpt da transcript

good afternoon everyone and welcome to three surprising kubernetes networking features and how to defend against them so just a little bit of a background about me uh i used to be a penetration tester and these days i work at control plane uh predominantly being a security consultant but i also help out with training and workshops and contribute to our ctf events such as the one we ran at cloud native security days so what are we going to talk about today we're going to run through the external attack surface of a kubernetes cluster having a little bit of look at what we can discover having a little bit of a look at some of the underlying primitives of the cluster and some ways that we can abuse them we'll take a little bit of a deeper dive into some cni primitives in two separate parts and then we'll run through how we can defend against the attacks that we mentioned so why do we care about any of this typically in a kubernetes assessment a security assessment in my experience will start from the perspective of a compromised workload a compromise pod maybe we assume that a developer laptop's been compromised but there is still some attack service that is not accounted for let's have a look at what we can get from an authentic and authenticated perspective in the network using some more classical techniques so we're going to start by having a look at open ports on our nodes so if you use one of our favorite port mapping tools and take a typical worker node we might expect something like this to show up uh so as we're using linux kubernetes nodes uh it's fairly typical to expect ssh to be open but port 10256 and 10 2 5 0 are kubernetes components we can verify this just by jumping on one of the machines and verifying that q proxy owns 10.256 and this exposes a healthy health check api which doesn't really have too much attack surface so we'll move on port 10250 is a little bit more interesting as this is the cubelet api in modern versions of kubernetes this is authenticated however and so from a perspective on the network where we don't have any credentials there's not much to see here on that topic however if we did find any credentials um there's an excellent tool um cybrok called cubelet ctl that actually documents this api it's a little bit outside of the scope of the talk today so if we move on to what a control plane load might look like uh in in a self-managed cluster we can see some familiar ports from the worker node um so we've still got those cub
