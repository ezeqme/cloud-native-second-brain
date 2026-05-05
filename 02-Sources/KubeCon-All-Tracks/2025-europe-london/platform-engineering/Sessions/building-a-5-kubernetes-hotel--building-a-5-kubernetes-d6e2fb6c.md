---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Observability", "Platform Engineering", "Kubernetes Core"]
speakers: ["Dean Fuller", "Fidelity International", "Rachael Wonnacott", "Fidelity International"]
sched_url: https://kccnceu2025.sched.com/event/1txAE/building-a-5-kubernetes-hotel-dean-fuller-fidelity-international-rachael-wonnacott-fidelity-international
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+5%2A+Kubernetes+Hotel+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Building a 5* Kubernetes Hotel - Dean Fuller, Fidelity International & Rachael Wonnacott, Fidelity International

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Observability]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Dean Fuller, Fidelity International, Rachael Wonnacott, Fidelity International
- Schedule: https://kccnceu2025.sched.com/event/1txAE/building-a-5-kubernetes-hotel-dean-fuller-fidelity-international-rachael-wonnacott-fidelity-international
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+5%2A+Kubernetes+Hotel+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Building a 5* Kubernetes Hotel.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAE/building-a-5-kubernetes-hotel-dean-fuller-fidelity-international-rachael-wonnacott-fidelity-international
- YouTube search: https://www.youtube.com/results?search_query=Building+a+5%2A+Kubernetes+Hotel+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ahANKkTT-yo
- YouTube title: Building a 5* Kubernetes Hotel - Dean Fuller & Rachael Wonnacott
- Match score: 0.739
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/building-a-5-kubernetes-hotel/ahANKkTT-yo.txt
- Transcript chars: 36205
- Keywords: platform, actually, customers, rachel, infrastructure, organization, fidelity, engineering, little, probably, features, developers, applications, mentioned, product, developer, cluster, foundry

### Resumo baseado na transcript

Thank you very much for coming to our talk today on building a five-star Kubernetes hotel. We'll introduce ourselves and then dive straight in because we want to make the most of the 30 minutes. But over time we recognized that the cloud foundry community was diminishing and over the last 10 years given the number of you in the audience I think it's fair to say that Kubernetes has dominated the market. We do buy and we do have merges between those pieces of software and we found that lots of these third parties were expecting Kubernetes to be within our organization be it they providing Helm charts or something of that nature. Also from a career vitality perspective we want to have the best engineers and to have the best engineers you probably want to be using the best technologies and we felt that that career vitality would come with Kubernetes and probably not with Cloud Foundry. Finally, we had several business applications that were already tied in with certain products, for example, the Bloomberg API and they were also expecting Kubernetes to run.

### Excerpt da transcript

Thank you very much for coming to our talk today on building a five-star Kubernetes hotel. We'll introduce ourselves and then dive straight in because we want to make the most of the 30 minutes. So my name is Rachel Wanott and I'm the technical product owner for the Kubernetes platform at Fidelity International. I'll let him introduce himself, but this is Dean Fuller who has the wonderful job of looking after me. Thank you Rachel. So hi everybody. I'm uh Dean Fuller. I look after what is known as developer platform engineering at Fidelity. Some of you might have heard of Fidelity International. You may have pensions or personal investments with them, but Fidelity have been around since 1969. We operate in 27 countries and we look after 950 billion of people's money. So, Fidelity have actually been on our cloud journey since 2013. And that first started with Cloud Foundry on premise and it's actually been hugely successful in the organization. Over the last seven years, we've been on our public cloud journey in the way of AWS and Azure.

And that supports the two and a half thousand developers we have at Fidelity, delivering all the capabilities for our customers and internal systems. So today, you're going to hear me and Rachel talk about our customers. We follow the product model here at Fidelity. So when we're talking about customers, we're talking about our internal app devs at Fidelity. So let's get started on what that cloud model and operating model looks like at Fidelity. So as I say we went into cloud seven years ago and we very much did it on a very purist DevOps approach and the way we framed it is the cloud house effectively. Me and my platform engineering teams in in the organization would go and build the foundations for the house and we would then hand that over to our customers to be going and be able to build their houses that might host the customer applications or the internal business applications. And it was hugely successful when we launched this seven years ago. And today in Fidelity, we have over 600 houses across the organization where we've given people the freedom to go and build what they need for the organization.

Now Rachel has an absolutely fantastic video on this in the QR code you'll see in the corner there. So highly recommend you go away and take some time to watch that if you get a moment. But with this comes a shared responsibility model. The cloud platform team would go and deliver the foundation. So if you think of th
