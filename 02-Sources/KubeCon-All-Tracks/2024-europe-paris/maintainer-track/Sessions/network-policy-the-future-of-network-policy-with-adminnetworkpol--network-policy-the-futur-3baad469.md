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
themes: ["AI ML", "Security", "Networking", "Community Governance"]
speakers: ["Surya Seetharaman", "Andrew Stoycos", "Red Hat", "Hunter Gregory", "Microsoft"]
sched_url: https://kccnceu2024.sched.com/event/1Yhhb/network-policy-the-future-of-network-policy-with-adminnetworkpolicy-surya-seetharaman-andrew-stoycos-red-hat-hunter-gregory-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Network+Policy%3A+The+Future+of+Network+Policy+with+AdminNetworkPolicy+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Network Policy: The Future of Network Policy with AdminNetworkPolicy - Surya Seetharaman & Andrew Stoycos, Red Hat; Hunter Gregory, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Surya Seetharaman, Andrew Stoycos, Red Hat, Hunter Gregory, Microsoft
- Schedule: https://kccnceu2024.sched.com/event/1Yhhb/network-policy-the-future-of-network-policy-with-adminnetworkpolicy-surya-seetharaman-andrew-stoycos-red-hat-hunter-gregory-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Network+Policy%3A+The+Future+of+Network+Policy+with+AdminNetworkPolicy+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Network Policy: The Future of Network Policy with AdminNetworkPolicy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhhb/network-policy-the-future-of-network-policy-with-adminnetworkpolicy-surya-seetharaman-andrew-stoycos-red-hat-hunter-gregory-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Network+Policy%3A+The+Future+of+Network+Policy+with+AdminNetworkPolicy+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=riSv0g-TNtI
- YouTube title: Network Policy: The Future of Network Policy with AdminNetworkPolicy
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/network-policy-the-future-of-network-policy-with-adminnetworkpolicy/riSv0g-TNtI.txt
- Transcript chars: 31231
- Keywords: network, policy, policies, traffic, cluster, actually, namespace, allowed, saying, please, baseline, ingress, talking, spaces, tenants, feedback, working, around

### Resumo baseado na transcript

hi everyone Welcome to our talk it's about project updates on the network policy API work that we've been doing in the kubernetes Sig Community I'm sya and I'm an engineer working on the open shift networking team at Red Hat I'm also a contributor to the network policy API project and very very happy to be here at ccon with all of you and hi everybody I'm Hunter I work at Microsoft on uh Network policy and observability and today I'll be diving into user tooling uh very excited

### Excerpt da transcript

hi everyone Welcome to our talk it's about project updates on the network policy API work that we've been doing in the kubernetes Sig Community I'm sya and I'm an engineer working on the open shift networking team at Red Hat I'm also a contributor to the network policy API project and very very happy to be here at ccon with all of you and hi everybody I'm Hunter I work at Microsoft on uh Network policy and observability and today I'll be diving into user tooling uh very excited to show you guys a demo later and I'll pass it back yeah so let's get started with who are we right so um how many of you are hearing Network policies for the first time can we have a raise of hands that's perfect because everybody knows why you're here for right like so we are actually a subw working group within the Sig Network so special interest group network but we are a sub-working group within that group and we call ourselves the network policy API working group and we are mainly focused on developing new policy apis and maintaining the existing ones that we already have and these are basically the network policy API which is stable and we1 and has been around for a really long time 5 six years if I'm not wrong and it lives in the core kubernetes kubernetes repo and recently we've been working a lot on the next two apis which is what we'll be talking a lot about in the session which is the admin Network policy API and the base line admin Network policy apis so we'll dig a little more deeper into what those are and if you are interested in our code-based repo or our websites please um take the privilege to go and click on these links when you have the PDF from the skedge available so let's look a little bit into what network policy API is but I can see that a lot of you at least know what that is so that's good and I want to give a huge shout out to numerous contributors in the community who have made this possible so for the past so many years I don't even know the extensive list of contributors but um huge shout out to all of them for making this possible some of the use cases for Network policies and the reason behind why we have this API in the first place is the fact that it was designed keeping application developers in mind right so it was meant for namespace owners so as an application developer when you have your namespace and you put your apps on it security is an important perspective especially the networking security aspects of it so you might want to control what
