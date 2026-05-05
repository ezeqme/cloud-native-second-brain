---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Rajas Kakodkar", "VMware", "Amine Hilaly", "AWS"]
sched_url: https://kccnceu2024.sched.com/event/1YeQG/future-of-intelligent-cluster-ops-llm-azing-kubernetes-controllers-rajas-kakodkar-vmware-amine-hilaly-aws
youtube_search_url: https://www.youtube.com/results?search_query=Future+of+Intelligent+Cluster+Ops%3A+LLM-Azing+Kubernetes+Controllers+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Future of Intelligent Cluster Ops: LLM-Azing Kubernetes Controllers - Rajas Kakodkar, VMware & Amine Hilaly, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Rajas Kakodkar, VMware, Amine Hilaly, AWS
- Schedule: https://kccnceu2024.sched.com/event/1YeQG/future-of-intelligent-cluster-ops-llm-azing-kubernetes-controllers-rajas-kakodkar-vmware-amine-hilaly-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Future+of+Intelligent+Cluster+Ops%3A+LLM-Azing+Kubernetes+Controllers+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Future of Intelligent Cluster Ops: LLM-Azing Kubernetes Controllers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQG/future-of-intelligent-cluster-ops-llm-azing-kubernetes-controllers-rajas-kakodkar-vmware-amine-hilaly-aws
- YouTube search: https://www.youtube.com/results?search_query=Future+of+Intelligent+Cluster+Ops%3A+LLM-Azing+Kubernetes+Controllers+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=n9NJITZftFM
- YouTube title: Future of Intelligent Cluster Ops: LLM-Azing Kubernetes Controllers - Rajas Kakodkar & Amine Hilaly
- Match score: 0.905
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/future-of-intelligent-cluster-ops-llm-azing-kubernetes-controllers/n9NJITZftFM.txt
- Transcript chars: 30516
- Keywords: cluster, llm, upgrade, trying, actually, upgrades, controller, question, operations, another, wherein, basically, simulation, questions, controllers, delete, running, cannot

### Resumo baseado na transcript

welcome to this session on future of intelligent cluster operations uh can I get a show off hands of how many people made it to the Keynotes this morning okay so all of you all almost know have heard already about AI so welcome to yet another talk about AI um since we're going to talk about cluster operations uh let's start with the life of a kubernetes engineer but uh before that uh I'm Rogers uh I work at VM at broadcom uh I'm also involved in the cncf

### Excerpt da transcript

welcome to this session on future of intelligent cluster operations uh can I get a show off hands of how many people made it to the Keynotes this morning okay so all of you all almost know have heard already about AI so welcome to yet another talk about AI um since we're going to talk about cluster operations uh let's start with the life of a kubernetes engineer but uh before that uh I'm Rogers uh I work at VM at broadcom uh I'm also involved in the cncf technical Advisory Group runtime uh most specifically the working group around artificial intelligence in cncf as well as the working groups around wasum and things like that and I have Ain with me here yeah hi folks um my name is Amin I'm part of the AWS eks team I mostly work on controllers and uh recently uh llm nities so yeah pretty excited to to do this that's good next slide all right so life of kubernetes engineer so this is mostly what the life of kubernetes engineer looks like most of the times you're on on calls um and then we'll walk walk you through some of the other scenarios that we go through uh so this is this is what happens like you know you're good at deploying clusters you're all happy you go watch a movie and then you find out that a cluster cluster upgrade failed once the upgrade fails then you figure out that the uh apis that were there were deprecate ated and then eventually you have to restore the backup from ET CD uh Legend says that this is also a screenshot of someone who upgraded to 124 and didn't keep in mind the doish was removed and thoughts and prayers with them right now uh the other scenario that we mostly face is when we we've added all of the features we're doing good the stocks going off of our product and then we find CVS which we didn't resolve and have like you know led to the stock tanking uh so the point we're trying to make over here is kubernetes has become boring yet there are problems which uh are pain points uh in in this screenshot we can see that Reddit got down because of a kubernetes cluster upgrade um upgrading kubernetes clusters is not very easy or very seamless as of now because of multiple other reasons um similarly uh CV scannings upgrading uh bumping dependencies is also not very seamless so all in all debugging clusters when something goes down is still a pain Point uh what we're trying to focus on over here is how AI can help you uh a shout out to K GPD that recently got into cncf sandbox so this is like a step in the right direction wherein we w
