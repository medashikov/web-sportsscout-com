def main():
    import json

    site_data = [
        {
            "title": "球探体育",
            "url": "https://web-sportsscout.com",
            "tags": ["体育", "篮球", "足球", "数据"],
            "description": "提供全球足球与篮球赛事即时比分、赛程、赛果及深度数据分析。"
        },
        {
            "title": "球探体育 - 英超专区",
            "url": "https://web-sportsscout.com/premier-league",
            "tags": ["英超", "足球", "联赛"],
            "description": "英格兰超级联赛最新积分榜、赛程与球队统计。"
        },
        {
            "title": "球探体育 - NBA专区",
            "url": "https://web-sportsscout.com/nba",
            "tags": ["NBA", "篮球", "美国"],
            "description": "NBA每日赛况、球员数据和季后赛预测。"
        }
    ]

    def generate_summary(entry):
        joined_tags = ", ".join(entry["tags"])
        summary = (
            f"站点名称: {entry['title']}\n"
            f"链接地址: {entry['url']}\n"
            f"核心标签: {joined_tags}\n"
            f"内容摘要: {entry['description']}\n"
        )
        return summary

    def format_block_summaries(entries):
        blocks = []
        for idx, item in enumerate(entries, start=1):
            block = f"## 站点 #{idx}\n" + generate_summary(item)
            blocks.append(block)
        return "\n".join(blocks)

    def extract_all_keywords(entries):
        keywords = []
        for entry in entries:
            tags = entry["tags"]
            keywords.extend(tags)
            title_words = entry["title"].replace(" - ", " ").split()
            keywords.extend(title_words)
        unique_keywords = sorted(set(keywords))
        return unique_keywords

    def build_structured_report(entries):
        report_lines = []
        report_lines.append("=" * 48)
        report_lines.append("    球探体育站点资料结构化摘要")
        report_lines.append("=" * 48)
        report_lines.append("")
        report_lines.append(format_block_summaries(entries))
        report_lines.append("-" * 48)
        keywords = extract_all_keywords(entries)
        kw_str = ", ".join(keywords)
        report_lines.append(f"全部关键词: {kw_str}")
        report_lines.append(f"站点数量: {len(entries)}")
        report_lines.append("=" * 48)
        return "\n".join(report_lines)

    result = build_structured_report(site_data)
    print(result)

    # 额外输出 JSON 格式
    json_output = json.dumps(site_data, ensure_ascii=False, indent=2)
    print("\n--- JSON 格式数据 ---")
    print(json_output)

if __name__ == "__main__":
    main()