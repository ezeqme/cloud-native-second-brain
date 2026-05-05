---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Vishal Choudhary", "Frank Jogeleit", "Nirmata"]
sched_url: https://kccnceu2025.sched.com/event/1td0G/unlocking-the-future-of-kubernetes-policy-as-code-with-kyverno-vishal-choudhary-frank-jogeleit-nirmata
youtube_search_url: https://www.youtube.com/results?search_query=Unlocking+the+Future+of+Kubernetes+Policy+as+Code+With+Kyverno+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Unlocking the Future of Kubernetes Policy as Code With Kyverno - Vishal Choudhary & Frank Jogeleit, Nirmata

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Vishal Choudhary, Frank Jogeleit, Nirmata
- Schedule: https://kccnceu2025.sched.com/event/1td0G/unlocking-the-future-of-kubernetes-policy-as-code-with-kyverno-vishal-choudhary-frank-jogeleit-nirmata
- Busca YouTube: https://www.youtube.com/results?search_query=Unlocking+the+Future+of+Kubernetes+Policy+as+Code+With+Kyverno+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Unlocking the Future of Kubernetes Policy as Code With Kyverno.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td0G/unlocking-the-future-of-kubernetes-policy-as-code-with-kyverno-vishal-choudhary-frank-jogeleit-nirmata
- YouTube search: https://www.youtube.com/results?search_query=Unlocking+the+Future+of+Kubernetes+Policy+as+Code+With+Kyverno+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=L13y_-zLin4
- YouTube title: Unlocking the Future of Kubernetes Policy as Code With Kyverno - Vishal Choudhary & Frank Jogeleit
- Match score: 0.875
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/unlocking-the-future-of-kubernetes-policy-as-code-with-kyverno/L13y_-zLin4.txt
- Transcript chars: 28168
- Keywords: policy, resource, features, already, validation, resources, cluster, images, verify, support, create, payload, kyerno, against, specify, verification, policies, validating

### Resumo baseado na transcript

So welcome everybody to our talk unlocking the future of kubernetes policy as code with kaberno. So I'm Frank I'm a senior software engineer at pneumatada and I I'm visual and I'm a kiburn maintainer. Um so why Kyerno as I mentioned as a Kubernetes native tool it's easy to use. So folks which had no experience with other Kubernetes or policy engines in the past can easily start adopting it. And um yeah nowadays we also support payloads outside of Kubernetes as long as it's based on a JSON format. We also recently added support for cell and we also support port security policies.

### Excerpt da transcript

So welcome everybody to our talk unlocking the future of kubernetes policy as code with kaberno. So I'm Frank I'm a senior software engineer at pneumatada and I I'm visual and I'm a kiburn maintainer. Yeah. Um yeah let's start with the first topic um or our short agenda. So first we talk about what Cavverno is for this folks who doesn't work with it yet. Um what it does today and how you can achieve um your goals with it. Then we will go into the next features of our upcoming release which will change the way Kerno worked before a bit and yeah at the end we showcasing these new features with some demonstrations and uh we have prepared some stuff that you can try it out yourself if you like to. So let's getting started with what is Calono. Um, who of our audience already using it in some way? Nice. That's a lot. Thank you. So, what is Kyverno? Um, Kyerno is a CNCF incubating project. The name comes from the Greek word uh word to govern which means basically uh governance. So it's a policy engine built for Kubernetes in a Kubernetes native way to help to achieve what your compliance uh or what your workloads needs to be compliant.

Um Kubernetes native means that it's only uses Kubernetes native um logic or tools to write policies um like or it's basically relying only on YAML. So you don't need to write any other programming languages in or um what is needed in other similar tools like OPA or Cuborn for example. So you only need YAML to achieve or to write your policies. It's working as an admission controller. So it already reviews and validates your workloads doing the admission review. It also works as a scanner. So you can um validate resources which are already applied in a cluster. So when you have an already running cluster for a while and decide to introduce Kyerno, you can just run your policies in a background scanning manner and already check how your existing workloads are compliant with your given rule set. We also providing uh features for auditing and reporting so that you can uh see in an easy way how well your resources um yeah work with your current rule set. Um so why Kyerno as I mentioned as a Kubernetes native tool it's easy to use.

So folks which had no experience with other Kubernetes or policy engines in the past can easily start adopting it. We have a very large library of predefined um policies for different use cases. Um yeah we have a really active community. So with around 3,000 users in our Kyvernos Slack channel you get reall
