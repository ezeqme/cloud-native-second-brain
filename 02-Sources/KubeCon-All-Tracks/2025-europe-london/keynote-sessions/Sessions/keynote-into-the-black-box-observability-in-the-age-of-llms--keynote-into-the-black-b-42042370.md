---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Keynote Sessions"
themes: ["AI ML", "Observability"]
speakers: ["Christine Yen", "CEO and Cofounder", "Honeycomb"]
sched_url: https://kccnceu2025.sched.com/event/1txBR/keynote-into-the-black-box-observability-in-the-age-of-llms-christine-yen-ceo-and-cofounder-honeycomb
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Into+the+Black+Box%3A+Observability+in+the+Age+of+LLMs+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: Into the Black Box: Observability in the Age of LLMs - Christine Yen, CEO and Cofounder, Honeycomb

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Christine Yen, CEO and Cofounder, Honeycomb
- Schedule: https://kccnceu2025.sched.com/event/1txBR/keynote-into-the-black-box-observability-in-the-age-of-llms-christine-yen-ceo-and-cofounder-honeycomb
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Into+the+Black+Box%3A+Observability+in+the+Age+of+LLMs+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: Into the Black Box: Observability in the Age of LLMs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txBR/keynote-into-the-black-box-observability-in-the-age-of-llms-christine-yen-ceo-and-cofounder-honeycomb
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Into+the+Black+Box%3A+Observability+in+the+Age+of+LLMs+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=R0255efML-I
- YouTube title: Keynote: Into the Black Box: Observability in the Age of LLMs - Christine Yen
- Match score: 0.974
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-into-the-black-box-observability-in-the-age-of-llms/R0255efML-I.txt
- Transcript chars: 12983
- Keywords: observability, llm, software, behavior, inputs, prompt, systems, capture, experience, metadata, trying, engineering, production, impact, application, ultimately, everything, whether

### Resumo baseado na transcript

While I am the co-founder and CEO of Honeycomb, I will say the statements and assertions I make should apply to any modern observability workflow. It's very cool to be in the middle of a phase change in progress when everything is new to everyone at the same time. So, is it time to give up on everything we've learned and know how to do and just embrace the rise of prompt engineering as a specialized skill set of the future? Whether that complexity comes from your architecture or trying to understand the business impact or per user experiences. and SLOs's service level objectives borrowed from our SRE friends have let us leverage existing alerting workflows but anchoring them around fuzzy concepts like user experience or are we delivering a good service to our end users these trends have already begun driving a distinct Now, observability helps embrace some unpredictability, enabling the sort of feedback loops that let you learn from what's really happening with your code.

### Excerpt da transcript

Hello, my name is Christine Yen. Thank you for having me. I'm excited to be here. While I am the co-founder and CEO of Honeycomb, I will say the statements and assertions I make should apply to any modern observability workflow. Let's get in. Writing software today feels more magical than it ever has before. We've got LLMs everywhere. We have cheap API calls to foundation models. Not even going to touch the whole idea of vibe coding in this talk. There's a lot to be excited about here. It's very cool to be in the middle of a phase change in progress when everything is new to everyone at the same time. And most of us here today have been building software before this LLM boom. And we know the hard part about building software systems isn't just the writing of the code. It's the testing. It's the maintenance, the tuning, and the debugging that comes after. So, while LLMs have a ton of implications for everything that we're doing, I want to spend this time with you today on this specific part of it. How we make sure that the code that we build on top of these magical black boxes still works the way that we expect after we've shipped and it's in front of the user.

Now, we work with black boxes and software all the time, but LLMs take some of the ways that we're used to ensuring consistent, reliable behavior and make them a little more difficult. Take for example trying to make sure your code overall is testable, mockable, and debugable. Well, unit tests rely on your being able to define a representative set of inputs. With LLMs, we're intentionally opening the door to a very long tale of possible inputs. As for mocks, LLMs are by nature nondeterministic. Swapping it out for deterministic mock doesn't really help us much here. And when it comes to debugging your LLM behavior, we don't have simple logical paths to step through. The whole point of incorporating LLMs into our software is to wrap the full breadth of human expression into our code. Debugging LLM behaviors kind of just turns out to trying something and seeing what happens. So this turning upside down of our worldview is happening on a literal software engineering systems engineering level where these black boxes just aren't testable or debugable the way that we're used to, which means there's no solid sense of correct to fall back to.

It's also true at a meta level. There is no environment within which we can conduct our tests and feel confident in the results. Even normal product development or re
