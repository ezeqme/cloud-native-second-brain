---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/metrics-explorer-a-tool-used-to-learn-about-prometheus/
youtube_url: https://www.youtube.com/watch?v=Yf3vjLAo2gg
youtube_search_url: https://www.youtube.com/results?search_query=Metrics+Explorer%3A+A+tool+used+to+learn+about+Prometheus%2C+gain+insight+into+metrics+and+search+metrics+dynamically+PromCon+2023
video_match_score: 0.914
status: video-found
---

# Metrics Explorer: A tool used to learn about Prometheus, gain insight into metrics and search metrics dynamically

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/metrics-explorer-a-tool-used-to-learn-about-prometheus/
- YouTube: https://www.youtube.com/watch?v=Yf3vjLAo2gg

## Resumo

Speaker(s): Brendan O'Handley & Catherine Gui In Grafana, the challenge of frontend metric exploration becomes pronounced as some users contend with tens of thousands of metrics. Our insights from interviews reveal a keen user desire: the ability to dynamically navigate metrics and gain familiarity with their metric landscape. Addressing this need, we introduce the Metrics Explorer—a dynamic tool tailored for users of varying expertise levels.

## Abstract oficial

Speaker(s): Brendan O'Handley & Catherine Gui

In Grafana, the challenge of frontend metric exploration becomes pronounced as some users contend with tens of thousands of metrics. Our insights from interviews reveal a keen user desire: the ability to dynamically navigate metrics and gain familiarity with their metric landscape. Addressing this need, we introduce the Metrics Explorer—a dynamic tool tailored for users of varying expertise levels. The metrics explorer offers a flexible interface that adapts based on whether users begin their exploration with metric searches filtered by labels or vice versa, using intuitive tree diagrams to depict the relationships between metrics and labels. The metrics explorer has a variety of elements to enhance metric search and comprehension, featuring a concise tabular presentation of metric names, types, and descriptions, along with type-based filters guiding users to specific areas of interest, complemented by a fuzzy search for expedient discovery of metric names and descriptions. The results are paginated to manage lengthy lists while not truncating the actual list of metrics. Advanced users can leverage regex search for precise queries. Beyond facilitating metric exploration and insights, the metrics explorer facilitates informed decision-making in system monitoring and doubles as a valuable educational tool, nurturing the learning journey of newcomers.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/metrics-explorer-a-tool-used-to-learn-about-prometheus/
- YouTube: https://www.youtube.com/watch?v=Yf3vjLAo2gg
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Yf3vjLAo2gg
- YouTube title: PromCon 2023 - Metrics Explorer: A Tool Used To Learn About Prometheus, Gain Insight Into Metrics
- Match score: 0.914
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/metrics-explorer-a-tool-used-to-learn-about-prometheus-gain-insight-in/Yf3vjLAo2gg.txt
- Transcript chars: 24887
- Keywords: metrics, labels, metric, search, values, prometheus, explorer, grafana, wanted, within, research, feature, results, metadata, browser, testing, getting, product

### Resumo baseado na transcript

[Music] [Applause] hello uh we are here to present the metric metrics Explorer a tool used to learn about Prometheus um I'm Brendan oh' Handley a software engineer at grafana and I work on the metric data sources um so this includes the Prometheus data source in grafana and Katherine hey everyone I'm Katherine I'm a product designer of grafana also working with Brendan on the team that maintains metrix based data sources so today we'll be talking about something a little bit different a user focused case study on

### Excerpt da transcript

[Music] [Applause] hello uh we are here to present the metric metrics Explorer a tool used to learn about Prometheus um I'm Brendan oh' Handley a software engineer at grafana and I work on the metric data sources um so this includes the Prometheus data source in grafana and Katherine hey everyone I'm Katherine I'm a product designer of grafana also working with Brendan on the team that maintains metrix based data sources so today we'll be talking about something a little bit different a user focused case study on building the metrics explore cool thank you we are very happy to be here and we'll talk about the background of the metric Explorer why we build it can we give users more power to explore um the learnings from user testing and our next steps so a little bit about the background in 2022 grafana set a goal to improve the getting started experience for new users uh and we know historically grafana has catered towards power users and early adopters but we also knew that the um product could be challenging for new users especially Prometheus beginners U so we wanted to make getting started in Prometheus easier and to expand to more audiences um so we created the first cross functional planning to have a collaboration between ux product and engineering and with the spirit of collaboration guiding us we looked at our users workflow identified areas of biggest impact and Katherine and I that work on data sources we work on uh parts of grafana that involve configuring data sources and quering querying data so this was a great opportunity to look into and this research guided uh why we built what we built so the research plan it was put into place to understand how users interacted with prometh with the Prometheus data source and we wanted to focus on Prometheus in grafana because it's our most widely used data source and I want to say as an engineer um this was different than my normal work um but it was also very exciting and very eye-opening for me um what I got to see were I got to see clearly the gaps that uh new Prometheus users have and their knowledge um and it also allowed me to come up with ideas on how to solve for their pain points So This research included workshopping user Journey mapping Persona creation and interviewing users and we started with a workshop with grafana employees we brought together software Engineers we brought together ux uh researchers and product to provide Prov feedback on the whole getting started process um within this
