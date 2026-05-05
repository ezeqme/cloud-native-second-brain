---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Application Development"
themes: ["Application Development"]
speakers: ["Scott McAllister", "ngrok"]
sched_url: https://kccnceu2025.sched.com/event/1txBI/are-you-covered-falling-in-love-with-e2e-testing-scott-mcallister-ngrok
youtube_search_url: https://www.youtube.com/results?search_query=Are+You+Covered%3F+Falling+in+Love+With+E2E+Testing+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Are You Covered? Falling in Love With E2E Testing - Scott McAllister, ngrok

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[Application Development]]
- País/cidade: United Kingdom / London
- Speakers: Scott McAllister, ngrok
- Schedule: https://kccnceu2025.sched.com/event/1txBI/are-you-covered-falling-in-love-with-e2e-testing-scott-mcallister-ngrok
- Busca YouTube: https://www.youtube.com/results?search_query=Are+You+Covered%3F+Falling+in+Love+With+E2E+Testing+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Are You Covered? Falling in Love With E2E Testing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txBI/are-you-covered-falling-in-love-with-e2e-testing-scott-mcallister-ngrok
- YouTube search: https://www.youtube.com/results?search_query=Are+You+Covered%3F+Falling+in+Love+With+E2E+Testing+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=emjrmJZR-ZI
- YouTube title: Are You Covered? Falling in Love With E2E Testing - Scott McAllister, ngrok
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/are-you-covered-falling-in-love-with-e2e-testing/emjrmJZR-ZI.txt
- Transcript chars: 25412
- Keywords: github, testing, application, inside, running, action, changes, cluster, little, request, actually, process, production, configuration, values, config, repository, gitops

### Resumo baseado na transcript

I usually do a thing at the beginning of my talks to prove to my bosses that I went to a location and it actually did work. Didn't come to England just to watch soccer, although I did and it was fantastic. I know for me, I've learned projects by getting into the tests first, running those, seeing how they how they operate, how it affects the code, even tweaking them a little bit to make sure that I understand what's happening. But then also, it can make it can make for clear design and encourage productivity. So I want to share a demo that I built on a subject that's near and dear to my heart. So, I'm going to try to show all three of those to you today so that you can each of those different types of learning, you can kind of see what's going on.

### Excerpt da transcript

Thank you all for coming today. I need your help. I usually do a thing at the beginning of my talks to prove to my bosses that I went to a location and it actually did work. Didn't come to England just to watch soccer, although I did and it was fantastic. I need you all to help me out. Can you smile and wave? And this room is so big. We're going to do smile and wave there. Awesome. Thank you all. Put that away so we don't get distracted. If you are still here at CubeCon and you're in this room, you're going to learn a little bit about testing, specifically endtoend testing. And now I know each of you like me because we're software people. We're detail oriented. You read the description facidiously. You knew everything that I'm going to talk about today. So of course, not only we going to talk about testing, we're also going to talk a little bit about GitOps. Not a lot, but I do want to talk about the whole process, right? Where we take our code and we're going to build, test, and then deploy our application.

And then we're going to talk about a few GitOps principles in there too that I wanted to share. So testing, why do we do it? We do it to evaluate and verify that our code is going to act as expected. Because honestly, two of the most important things in software development is that we make sure that our code works and that we can push changes out quickly. Because if our code does something unexpected and if our users hit something unexpected, that's usually called a bug, right? And we don't want that. So with testing, we want to make sure we have our tests running, but we also have our tests automated so that we can push our changes out quickly and make sure that our software is running the latest things that we want, the latest features that we want our customers to use. Our good friend Adler also said this about testing. It can work as documentation. I know for me, I've learned projects by getting into the tests first, running those, seeing how they how they operate, how it affects the code, even tweaking them a little bit to make sure that I understand what's happening.

But then also, it can make it can make for clear design and encourage productivity. We have confidence that our changes are not going to adversely affect our systems as we push them out. So endtoend testing is that type of testing where we're going to be testing the entire flow. You have all different types of testing you could be doing in your software development. You have unit t
