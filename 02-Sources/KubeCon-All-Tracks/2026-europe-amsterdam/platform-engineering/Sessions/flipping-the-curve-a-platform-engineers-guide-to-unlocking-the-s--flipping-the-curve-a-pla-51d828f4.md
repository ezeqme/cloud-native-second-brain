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
themes: ["Platform Engineering"]
speakers: ["Michael Reichenbach", "1KOMMA5°"]
sched_url: https://kccnceu2026.sched.com/event/2CW89/flipping-the-curve-a-platform-engineers-guide-to-unlocking-the-silent-80-michael-reichenbach-1komma5deg
youtube_search_url: https://www.youtube.com/results?search_query=Flipping+the+Curve%3A+A+Platform+Engineer%27s+Guide+to+Unlocking+the+Silent+80%25+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Flipping the Curve: A Platform Engineer's Guide to Unlocking the Silent 80% - Michael Reichenbach, 1KOMMA5°

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Michael Reichenbach, 1KOMMA5°
- Schedule: https://kccnceu2026.sched.com/event/2CW89/flipping-the-curve-a-platform-engineers-guide-to-unlocking-the-silent-80-michael-reichenbach-1komma5deg
- Busca YouTube: https://www.youtube.com/results?search_query=Flipping+the+Curve%3A+A+Platform+Engineer%27s+Guide+to+Unlocking+the+Silent+80%25+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Flipping the Curve: A Platform Engineer's Guide to Unlocking the Silent 80%.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW89/flipping-the-curve-a-platform-engineers-guide-to-unlocking-the-silent-80-michael-reichenbach-1komma5deg
- YouTube search: https://www.youtube.com/results?search_query=Flipping+the+Curve%3A+A+Platform+Engineer%27s+Guide+to+Unlocking+the+Silent+80%25+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xRpGhFihQpk
- YouTube title: Flipping the Curve: A Platform Engineer's Guide to Unlocking the Silent 80% - Michael Reichenbach
- Match score: 0.958
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/flipping-the-curve-a-platform-engineers-guide-to-unlocking-the-silent/xRpGhFihQpk.txt
- Transcript chars: 30264
- Keywords: platform, actually, metrics, interviews, product, experts, measure, terraform, engineers, middle, problems, products, company, surveys, already, question, feature, survey

### Resumo baseado na transcript

Um today, I'm going to share a bit about my story and experience for platform engineering and how we can start building for the silent 80%. And who here knows this that you build something you're really are sure that it's going to work, that's people need it, but then in the end you keep on pushing it to people and nobody really uses it or only a fraction. Um you they're great if you're new to a team and you come to a company to actually get to know what are they using, what are the CI flows, how does Terraform look alike, how is the Kubernetes set up, and so on. These are the interviews you do to get to know the problems you don't know about. Before we start building, we actually want to know if there is more than five users that have these problems. When you're done these three to five user interviews, you should have a good understanding or list of hypotheses of problems in your platform, things you want to validate.

### Excerpt da transcript

Thank you everyone for coming. A full room. That's really great to see. Um today, I'm going to share a bit about my story and experience for platform engineering and how we can start building for the silent 80%. But what does that even mean? Before I start, I want to share a short story. Once upon a time, I built this awesome CLI. Could do everything. Connect to Jira, Kubernetes, deploy our services, read from Backstage. It was so cool. This was pre-AI, so built it with sweat and tears. And the users loved it. The one user loved it. I loved it. But yeah, um that's how it goes sometimes. And who here knows this that you build something you're really are sure that it's going to work, that's people need it, but then in the end you keep on pushing it to people and nobody really uses it or only a fraction. So, quick raise of hands, who's experienced this before? A lot. I'm not alone, that's good. >> [laughter] >> So, but why does it actually happen? Why do we keep sometimes building things nobody ends up using or only a few?

For this, let's look at who are we actually building for. This is oversimplified. So, we have platform engineers. Us, DevOps engineers. They're experts. Then on the other side of the spectrum, we have the other experts. This can be users who are proficient in Terraform, know Kubernetes, love Kubernetes, and can't imagine using anything else. Then in the middle, we have the average software engineer. And if we put them on a bell curve, the distribution in a company, you usually have the average engineers in the middle and on the sides you have only a fraction of those stupid people. Platform engineers and the experts. And the ones we actually want to build for are the ones in the middle. Right? So, the 80% in the middle are the ones that they need our platform the most because those are the ones that are not the experts, that are not proficient in Kubernetes or Terraform. But when we look at this, why do we keep building for ourselves and experts? That's because they're the loudest. That's the issue here.

The experts and we ourselves are very convinced what a problem is, what a good problem should be solved. The experts are very loud in telling us what they need, what they want. And that's where you can get biased and pulled towards the edges and forget about the silent in the middle. This creates what I call an inverse productivity curve where you have the edges, the platform engineers, the experts are highly productive in their very spec
