---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Keynote Sessions"
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Jorge Palma", "Principal PM Lead", "Microsoft"]
sched_url: https://kccnceu2024.sched.com/event/1YhJe/sponsored-keynote-build-an-open-source-platform-for-aiml-jorge-palma-principal-pm-lead-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Build+an+Open+Source+Platform+for+AI%2FML+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Sponsored Keynote: Build an Open Source Platform for AI/ML - Jorge Palma, Principal PM Lead, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Jorge Palma, Principal PM Lead, Microsoft
- Schedule: https://kccnceu2024.sched.com/event/1YhJe/sponsored-keynote-build-an-open-source-platform-for-aiml-jorge-palma-principal-pm-lead-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Build+an+Open+Source+Platform+for+AI%2FML+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Build an Open Source Platform for AI/ML.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhJe/sponsored-keynote-build-an-open-source-platform-for-aiml-jorge-palma-principal-pm-lead-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Build+an+Open+Source+Platform+for+AI%2FML+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=r7qd0ZHt4uE
- YouTube title: Sponsored Keynote: Build an Open Source Platform for AI/ML - Jorge Palma, Principal PM Lead
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sponsored-keynote-build-an-open-source-platform-for-ai-ml/r7qd0ZHt4uE.txt
- Transcript chars: 5163
- Keywords: models, actually, infrastructure, leverage, source, trying, requirements, deploy, inference, platform, throughout, conference, revolution, unlock, applications, little, started, gpu

### Resumo baseado na transcript

all right good morning cucon so AI is clearly the word of the day of the week you'll hear it echoed throughout the Halls you'll see it in the Keynotes amazing speakers great breakouts throughout the conference and it's no surprise we're truly living in the age of AI Revolution uh a lot of it has been said over the last months and how the AI train has departed a station and if you're like me you're trying to find ways to ensure that you're in it you're probably trying

### Excerpt da transcript

all right good morning cucon so AI is clearly the word of the day of the week you'll hear it echoed throughout the Halls you'll see it in the Keynotes amazing speakers great breakouts throughout the conference and it's no surprise we're truly living in the age of AI Revolution uh a lot of it has been said over the last months and how the AI train has departed a station and if you're like me you're trying to find ways to ensure that you're in it you're probably trying to see how you can actually use generative AI to unlock new scenarios to unlock new opportunities experiences for your customers and users internal or external you're trying to find at the end of the day a way to make your applications more intelligent today your applications might look a little bit like this maybe a bit more microservices maybe a little bit more monolithic hopefully in kubernetes and truly the easiest way to get started is really leveraging a SAS Service uh like open AI that really allows you to get started it super quickly prototype go fine-tune go all the way to production but a lot of you I'm sure have requirements that go a littleit beyond that you might actually have data residency requirements you might have compliance requirements you might want to have more control and flexibility you might even have existing infrastructure Investments on GPU capacity that you want to leverage to make it more economic so what we honestly see a lot these days is what we've been dubbing local models uh as in models deployed in your own infrastructure typically on VMS now as a lot of you known and as pranka mentioned container images are really a great format not just for software but also for models they're really easy to distribute you can keep both your code and your models uh in the same format and you can very easily manage a lot of them with the easy access to a registry moreover you can then deploy them into kubernetes and actually Leverage all the nice Primitives and abstraction that kubernetes gives you for for example managing that hetrogeneous infrastructure um and at do it at scale all right so job done right and we wanted local models throw it in kubernetes done not quite yet because even though this is easier it doesn't really make it easy you actually need to look at a number of steps to actually achieve that outcome starting from containerizing the models a lot of them are not containerized today second uh getting that GPU capacity into your cluster and bootstrapping it t
