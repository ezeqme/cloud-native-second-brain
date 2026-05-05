---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Application Development"
themes: ["SRE Reliability", "Community Governance"]
speakers: ["Michael Kuhnt", "Mercedes-Benz Tech Innovation", "Gabriel Adrian Samfira", "Cloudbase Solutions"]
sched_url: https://kccnceu2026.sched.com/event/2CVyi/from-open-source-to-enterprise-scale-and-back-a-journey-with-road-runner-michael-kuhnt-mercedes-benz-tech-innovation-gabriel-adrian-samfira-cloudbase-solutions
youtube_search_url: https://www.youtube.com/results?search_query=From+Open+Source+To+Enterprise+Scale+and+Back%3A+A+Journey+With+Road-Runner+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From Open Source To Enterprise Scale and Back: A Journey With Road-Runner - Michael Kuhnt, Mercedes-Benz Tech Innovation & Gabriel Adrian Samfira, Cloudbase Solutions

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Application Development]]
- Temas: [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Michael Kuhnt, Mercedes-Benz Tech Innovation, Gabriel Adrian Samfira, Cloudbase Solutions
- Schedule: https://kccnceu2026.sched.com/event/2CVyi/from-open-source-to-enterprise-scale-and-back-a-journey-with-road-runner-michael-kuhnt-mercedes-benz-tech-innovation-gabriel-adrian-samfira-cloudbase-solutions
- Busca YouTube: https://www.youtube.com/results?search_query=From+Open+Source+To+Enterprise+Scale+and+Back%3A+A+Journey+With+Road-Runner+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From Open Source To Enterprise Scale and Back: A Journey With Road-Runner.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyi/from-open-source-to-enterprise-scale-and-back-a-journey-with-road-runner-michael-kuhnt-mercedes-benz-tech-innovation-gabriel-adrian-samfira-cloudbase-solutions
- YouTube search: https://www.youtube.com/results?search_query=From+Open+Source+To+Enterprise+Scale+and+Back%3A+A+Journey+With+Road-Runner+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=eqX6w8bFyxE
- YouTube title: From Open Source To Enterprise Scale and Back: A Journey... Michael Kuhnt & Gabriel Adrian Samfira
- Match score: 0.86
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-open-source-to-enterprise-scale-and-back-a-journey-with-road-runn/eqX6w8bFyxE.txt
- Transcript chars: 23915
- Keywords: runners, github, runner, course, platform, source, workflow, instance, already, running, create, enterprise, provider, access, actually, repository, workflows, started

### Resumo baseado na transcript

Thanks for joining our talk from open source to enterprise scale and back, a journey with Roadrunner. In this talk, we want to share some lessons we learned while building a rather large managed shared service for our internal development teams at Mercedes-Benz based on open source project built by Gabriel and his team called Garm. When every team does it themselves, you have basically no room for standardization and also from a security perspective, this is rather concerning. Yeah, we want to have less duplicate work, more standardization, and security. So, whenever we had to make a design decision, we could come back to this document and see if we are still on track with our vision, what we actually wanted to build to help our developers. You would when you would contribute, your pull request would start running inside their own Jenkins instance, but you wouldn't be able to see the logs that that were generated.

### Excerpt da transcript

So, let's start. Hi. Thanks for joining our talk from open source to enterprise scale and back, a journey with Roadrunner. So, I'm Michael. I'm software engineer at Mercedes-Benz Tech Innovation. I'm Gabriel. I'm engineer at Cloud Base Solutions. In this talk, we want to share some lessons we learned while building a rather large managed shared service for our internal development teams at Mercedes-Benz based on open source project built by Gabriel and his team called Garm. But of course, it's not the idea to share you another awesome success story. It's more about the winding and uncertain path that it actually was building such a platform with a relatively small team and now it's used by thousands of users in our company. And in the beginning, I think nobody even knew that we needed such a platform. And take it a step back. So, maybe you've been there. Maybe you you've seen that too. You you have you see that opportunity in your department, in your company. You see an awesome new technology or a tool or a workflow that could help and enable a lot of developers.

But you don't have the time, the budget, or team, or even the mandate to do so. That was exactly our situation. So, how do you start? How do you not let this opportunity pass by? Let me show you our challenge, our problem. So, at Mercedes-Benz, we have GitHub Enterprise instance. And of course, it is not the only forge that we have at Mercedes, but I would say a larger portion of our source code is in this GitHub repository. instance. And it comes with all the bells and whistles as you would have it in github.com including GitHub Actions, which is GitHub's internal CICD and workflow platform. But for us, it didn't come with runners. So, the actual physical machines that would run these workflows. And this was a big problem. Because I mean, teams needed that and they got creative. And of course, they started building up their own little runner setups, which is totally okay in GitHub. That is possible, but it creates a lot of duplicate effort. When every team does it themselves, you have basically no room for standardization and also from a security perspective, this is rather concerning.

So, um we knew we had to do something and we knew we could do something because just looking at github.com, you have runners available in every repository just ready to use. So, we wrote we had a vision and we wrote it down. Of course, it sounds super simple and it is simple. So, you start with a design doc. You
