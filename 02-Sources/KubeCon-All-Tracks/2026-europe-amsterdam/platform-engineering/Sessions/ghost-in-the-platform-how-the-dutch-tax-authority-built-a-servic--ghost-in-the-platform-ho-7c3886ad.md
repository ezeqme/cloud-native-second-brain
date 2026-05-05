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
themes: ["Platform Engineering", "SRE Reliability"]
speakers: ["Jerry van Hulst", "Belastingdienst", "Marcel Kerker", "HCS Company B.V."]
sched_url: https://kccnceu2026.sched.com/event/2CW3G/ghost-in-the-platform-how-the-dutch-tax-authority-built-a-service-to-scale-k8s-to-99+-applications-jerry-van-hulst-belastingdienst-marcel-kerker-hcs-company-bv
youtube_search_url: https://www.youtube.com/results?search_query=Ghost+in+the+Platform%3A+How+the+Dutch+Tax+Authority+Built+a+Service+To+Scale+K8s+To+99%2B+Applications+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Ghost in the Platform: How the Dutch Tax Authority Built a Service To Scale K8s To 99+ Applications - Jerry van Hulst, Belastingdienst & Marcel Kerker, HCS Company B.V.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jerry van Hulst, Belastingdienst, Marcel Kerker, HCS Company B.V.
- Schedule: https://kccnceu2026.sched.com/event/2CW3G/ghost-in-the-platform-how-the-dutch-tax-authority-built-a-service-to-scale-k8s-to-99+-applications-jerry-van-hulst-belastingdienst-marcel-kerker-hcs-company-bv
- Busca YouTube: https://www.youtube.com/results?search_query=Ghost+in+the+Platform%3A+How+the+Dutch+Tax+Authority+Built+a+Service+To+Scale+K8s+To+99%2B+Applications+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Ghost in the Platform: How the Dutch Tax Authority Built a Service To Scale K8s To 99+ Applications.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3G/ghost-in-the-platform-how-the-dutch-tax-authority-built-a-service-to-scale-k8s-to-99+-applications-jerry-van-hulst-belastingdienst-marcel-kerker-hcs-company-bv
- YouTube search: https://www.youtube.com/results?search_query=Ghost+in+the+Platform%3A+How+the+Dutch+Tax+Authority+Built+a+Service+To+Scale+K8s+To+99%2B+Applications+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PUHAYSM_jGI
- YouTube title: Ghost in the Platform: How the Dutch Tax Authority Built a Servi... Jerry van Hulst, & Marcel Kerker
- Match score: 0.796
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/ghost-in-the-platform-how-the-dutch-tax-authority-built-a-service-to-s/PUHAYSM_jGI.txt
- Transcript chars: 18130
- Keywords: platform, application, developers, applications, request, container, clusters, environment, started, infrastructure, customers, everything, production, question, deploy, journey, cluster, capabilities

### Resumo baseado na transcript

But what amazing people here a lot of people do you know that you really are in the same room or the correct room because maybe in other room no okay um we talk about our coin platform we start the journey Jerry what's about it >> well let's start with the beginning uh we are from the Dutch tax authority or as the Dutch people might know us as the bloing means I will refer to us as the bloss from here uh we We are part of the This mission is uh brought by us our product manager and um we talk in this talk about how how is our journey uh Gary what's our journey our journey starts in about 2017 where a group of engineers a new technology called kubernetes and It was very difficult for engineers that had never worked with Open Shift, never worked with Kubernetes to all of a sudden be required to know Arbback, Argo CD, network policies. What was first landing on the platform starting and deploying your first application in a matter of hours started to turn in weeks or months from provisioning the cluster to onboarding your application on the cluster to learning all the new tools. Um there with uh intake we have with a lot of questionary almost uh about 50 uh questions question questions about uh um the if if they used in health checks or readiness checks or what what kind of database they are using or what kind of loing can application scale or not.

### Excerpt da transcript

Welcome uh our presentation about coina platform. But what amazing people here a lot of people do you know that you really are in the same room or the correct room because maybe in other room no okay um we talk about our coin platform we start the journey Jerry what's about it >> well let's start with the beginning uh we are from the Dutch tax authority or as the Dutch people might know us as the bloing means I will refer to us as the bloss from here uh we We are part of the Dutch government. We are responsible for the collection of taxes, payment of benefits, and enforcement of customs. We are what some of you may know as the most hated company in the Netherlands. For such a hated company, we do have a lot of employees. over 28,000 people spread over the Netherlands, among which are 4,000 IT personnel. Last year, we collected over 300 billion euros in taxes. That is taxes from uh citizens, businesses, tourists. If you are in the Netherlands, you probably came across us. We have a vast IT landscape with a rich history spanning back over 60 years, but we're going to be focusing on the last 10.

We only have 30 minutes. >> My name is Janst. I am the product owner for the container hosting platform team. >> Yes. And my name is Mosker. I am a a consultant at HCS company and also part of the platform team and also I am a a CNCF ambassador. So um what was what is our mission? Our mission sent here is to empower the velocities the stack office uh with a platform and tools to take full ownership of a digital future. This mission is uh brought by us our product manager and um we talk in this talk about how how is our journey uh Gary what's our journey our journey starts in about 2017 where a group of engineers a new technology called kubernetes and a vision came together they wanted to create a platform with one thing in mind and that is maximum developer autonomy we would build build the platform they would run We started by building and automating the infrastructure and by doing so we created the foundation for what is still to this day our container hosting platform. The first years were focused on building the platform and in about 2019 the first customers started joining the platform really our early adopter phase and everything was going absolutely amazing.

Enthusiasm was high, adoption was growing and developer velocity was skyrocketing. During the same time, we also founded our enablement team where Marcel is part of. But not everything was great. Well, th
