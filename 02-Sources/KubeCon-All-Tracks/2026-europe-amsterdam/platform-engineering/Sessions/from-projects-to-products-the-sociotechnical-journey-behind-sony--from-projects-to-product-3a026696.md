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
themes: ["AI ML", "Platform Engineering"]
speakers: ["Eugenia Bergman", "Hagen Tonnies", "Sony Interactive Entertainment"]
sched_url: https://kccnceu2026.sched.com/event/2CW29/from-projects-to-products-the-sociotechnical-journey-behind-sonys-internal-cloud-platform-eugenia-bergman-hagen-tonnies-sony-interactive-entertainment
youtube_search_url: https://www.youtube.com/results?search_query=From+Projects+to+Products%3A+The+Sociotechnical+Journey+Behind+Sony%E2%80%99s+Internal+Cloud+Platform+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From Projects to Products: The Sociotechnical Journey Behind Sony’s Internal Cloud Platform - Eugenia Bergman & Hagen Tonnies, Sony Interactive Entertainment

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Eugenia Bergman, Hagen Tonnies, Sony Interactive Entertainment
- Schedule: https://kccnceu2026.sched.com/event/2CW29/from-projects-to-products-the-sociotechnical-journey-behind-sonys-internal-cloud-platform-eugenia-bergman-hagen-tonnies-sony-interactive-entertainment
- Busca YouTube: https://www.youtube.com/results?search_query=From+Projects+to+Products%3A+The+Sociotechnical+Journey+Behind+Sony%E2%80%99s+Internal+Cloud+Platform+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From Projects to Products: The Sociotechnical Journey Behind Sony’s Internal Cloud Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW29/from-projects-to-products-the-sociotechnical-journey-behind-sonys-internal-cloud-platform-eugenia-bergman-hagen-tonnies-sony-interactive-entertainment
- YouTube search: https://www.youtube.com/results?search_query=From+Projects+to+Products%3A+The+Sociotechnical+Journey+Behind+Sony%E2%80%99s+Internal+Cloud+Platform+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zrXvt9DXQ3U
- YouTube title: From Projects to Products: The Sociotechnical Journey Behind Sony... Eugenia Bergman & Hagen Tonnies
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-projects-to-products-the-sociotechnical-journey-behind-sonys-inte/zrXvt9DXQ3U.txt
- Transcript chars: 29801
- Keywords: platform, essentially, actually, started, obviously, trying, engineering, whether, little, infrastructure, capability, journey, product, needed, another, certain, having, projects

### Resumo baseado na transcript

Um we are very happy and excited to have you here today and take you on our journey of building uh our sociote technical journey on building the internal cloud platform at Sony PlayStation. Before we start, uh, I would actually like you to take a journey with me and to take you to a situation that I'm sure a lot of you are familiar with. I was data engineering, software engineering and now platform engineering and um yeah I work with CTFs and help uh facilitate their objectives obviously but making it also within a harmonized architecture and I bring a little bit the architecture perspective into the talk because Um, but where to through the moments where things looked like they were working but didn't exactly scale as we were expecting. We'll show you how we started by trying to solve this as a technical problem. We then uh moved on to a part where things started to break down at some point because even as the architecture itself improved the coordination between didn't quite scale as um following the architecture and finally how we had to rethink the problem entirely

### Excerpt da transcript

Good morning everyone. I hope that you've been enjoying the conference so far. Um we are very happy and excited to have you here today and take you on our journey of building uh our sociote technical journey on building the internal cloud platform at Sony PlayStation. Before we start, uh, I would actually like you to take a journey with me and to take you to a situation that I'm sure a lot of you are familiar with. You are part of a platform team. You've been running Kubernetes in production for years. You've built operators, pipelines, golden paths. You've standardized everything you could have standardized. So from the outside your platform looks very mature and yet somehow your backlog keeps on growing. Um, every team seems to need something slightly different and some ask for exceptions, others bypass your platform entirely. And you start seeing things like custom deployments, direct access to clusters, uh, teams reinventing parts of your stack and not because they want to break the rules, but simply because your platform doesn't fit their reality entirely.

And this is exactly where we ended ourselves in this situation. And Hagen and I are here today uh to tell you about our journey scaling both our internal cloud platform as well as the organization operating it uh Sony Interactive Entertainment which is the company behind PlayStation. So our goal today is not to tell you what you should be doing in your own scope, but rather share some of the learnings that we acquired over time, some signals that we learned to recognize, and hopefully some takeaways um that you can take out of this talk, some practical things. Um I would also like to share a message of hope. Moving from projects to products doesn't mean that you need an army of product managers. As a matter of fact, it's not a function that we have access to internally. And I think it's could be something that is quite advantageous because it requires you to put yourselves into the customer's shoes and really understand what their needs are and how do they experience your platform. And so starting as well with introducing ourselves a little bit more.

I'm Eugene Bergman. I work in the uh what we call the technical operations department within the uh gaming developer and future technology group at Sony PlayStation and I have been running for several years now large programs across infrastructure and platform engineering and recently I shifted a little bit my focus uh in helping teams to move from a
