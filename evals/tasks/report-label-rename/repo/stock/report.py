def render(rows: list[tuple[str, int]]) -> str:
    """A plain-text table of (name, count) rows, then a summary line."""
    lines = ["Item      Qty"]
    lines += [f"{name:<10}{count}" for name, count in rows]
    lines.append(f"Total Qty: {sum(count for _, count in rows)}")
    return "\n".join(lines)
